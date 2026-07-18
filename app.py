import os
import sys
import json
import subprocess
import shutil
import uuid

from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__, template_folder="templates")

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)


def ffprobe_duration(path: str) -> float:
    """Devuelve la duración del video en segundos usando ffprobe."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        path,
    ]
    out = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode().strip()
    return float(out)


def autoincrement_name(directory: str, base: str, ext: str) -> str:
    """Genera un nombre `<base>_cut_N<ext>` autoincrementado sin sobrescribir."""
    n = 1
    while True:
        candidate = f"{base}_cut_{n}{ext}"
        if not os.path.exists(os.path.join(directory, candidate)):
            return candidate
        n += 1


def parse_time_seconds(value):
    try:
        return max(0.0, float(value))
    except (TypeError, ValueError):
        return 0.0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "video" not in request.files:
        return jsonify({"error": "No se envió ningún archivo."}), 400
    f = request.files["video"]
    if not f.filename:
        return jsonify({"error": "Archivo vacío."}), 400

    safe_name = f"{uuid.uuid4().hex}_{f.filename}"
    dst = os.path.join(UPLOAD_DIR, safe_name)
    f.save(dst)

    try:
        duration = ffprobe_duration(dst)
    except Exception as e:
        os.remove(dst)
        return jsonify({"error": f"No se pudo leer el video (¿FFmpeg instalado?): {e}"}), 500

    return jsonify({
        "id": safe_name,
        "name": f.filename,
        "path": dst,
        "duration": duration,
    })


@app.route("/uploads/<path:fname>")
def serve_upload(fname):
    return send_from_directory(UPLOAD_DIR, fname)


@app.route("/cut", methods=["POST"])
def cut():
    data = request.get_json(force=True)
    src_path = data.get("path")
    start = parse_time_seconds(data.get("start", 0))
    end = parse_time_seconds(data.get("end", 0))

    if not src_path or not os.path.exists(src_path):
        return jsonify({"error": "Archivo de origen no encontrado."}), 400
    if end <= start:
        return jsonify({"error": "El tiempo de fin debe ser mayor que el de inicio."}), 400

    directory = os.path.dirname(src_path)
    original_name = os.path.basename(src_path)
    base, ext = os.path.splitext(original_name)
    # Quitamos el uuid que añadimos al guardar
    if "_" in base:
        base = base.split("_", 1)[1] if "_" in base else base
    # Si el upload se hizo en uploads/ y el usuario subió su propio archivo,
    # guardamos el corte en uploads/ junto al original tal cual exige el requisito
    # "misma ruta/carpeta que el video original".
    out_name = autoincrement_name(directory, f"{base}", ext)
    out_path = os.path.join(directory, out_name)

    cmd = [
        "ffmpeg", "-y",
        "-ss", f"{start:.3f}",
        "-to", f"{end:.3f}",
        "-i", src_path,
        "-c", "copy",
        "-avoid_negative_ts", "1",
        out_path,
    ]

    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if proc.returncode != 0 or not os.path.exists(out_path):
            return jsonify({
                "error": "FFmpeg falló al cortar el video.",
                "log": proc.stdout[-3000:],
            }), 500
    except FileNotFoundError:
        return jsonify({"error": "FFmpeg no está instalado en el sistema."}), 500

    # El corte fue exitoso: eliminamos el original de uploads/
    # para no duplicar espacio en disco. Solo queda el recortado.
    try:
        if os.path.exists(src_path) and os.path.abspath(src_path) != os.path.abspath(out_path):
            os.remove(src_path)
    except OSError:
        pass

    return jsonify({
        "output_path": out_path,
        "output_name": out_name,
        "directory": directory,
        "start": start,
        "end": end,
    })


@app.route("/open-file", methods=["POST"])
def open_file():
    data = request.get_json(force=True)
    path = data.get("path")
    if not path or not os.path.exists(path):
        return jsonify({"error": "Ruta inválida."}), 400
    try:
        if sys.platform.startswith("win"):
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.run(["open", path])
        else:
            subprocess.run(["xdg-open", path])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"ok": True})


@app.route("/open-folder", methods=["POST"])
def open_folder():
    data = request.get_json(force=True)
    path = data.get("path")
    if not path or not os.path.exists(path):
        return jsonify({"error": "Ruta inválida."}), 400
    directory = os.path.dirname(path)
    try:
        if sys.platform.startswith("win"):
            subprocess.run(["explorer", "/select,", os.path.normpath(path)])
        elif sys.platform == "darwin":
            subprocess.run(["open", "-R", path])
        else:
            subprocess.run(["xdg-open", directory])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"ok": True})


@app.route("/clean", methods=["POST"])
def clean():
    """Limpia los archivos temporales de la carpeta uploads."""
    try:
        for fn in os.listdir(UPLOAD_DIR):
            fp = os.path.join(UPLOAD_DIR, fn)
            if os.path.isfile(fp):
                os.remove(fp)
    except Exception:
        pass
    return jsonify({"ok": True})


if __name__ == "__main__":
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        print("ADVERTENCIA: FFmpeg/ffprobe no encontrados en PATH.")
    app.run(host="127.0.0.1", port=8013, debug=True)