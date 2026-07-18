# VideosCortador

Aplicación local con interfaz web para cortar videos **sin pérdida de calidad** usando FFmpeg (`-c copy`).

## Requisitos

1. **Python 3.9+**
2. **FFmpeg** (incluye `ffmpeg` y `ffprobe`) instalado y en el PATH del sistema.

## Instalación

```bash
cd C:\Users\yamil\Desktop\videoscortador
python -m venv .venv
.venv\Scripts\activate          # En Windows
# source .venv/bin/activate      # En macOS/Linux
pip install -r requirements.txt
```

## Instalar FFmpeg

### Windows
- Opción rápida: `winget install Gyan.FFmpeg`
- O manual: descarga desde https://www.gyan.dev/ffmpeg/builds/ → extrae y agrega la carpeta `bin` al PATH.

### macOS
```bash
brew install ffmpeg
```

### Linux (Debian/Ubuntu)
```bash
sudo apt update && sudo apt install -y ffmpeg
```

Verifica con:
```bash
ffmpeg -version
ffprobe -version
```

## Ejecutar

```bash
python app.py
```

Abre en el navegador: **http://127.0.0.1:5000**

## Uso

1. Arrastra el video a la zona punteada o usa **Seleccionar video**.
2. Mueve los dos controles del slider o escribe minutos/segundos.
3. Pulsa **Cortar video** → el corte se guarda junto al original como `video_cut_1.mp4`, `video_cut_2.mp4`, etc.
4. En la tarjeta de éxito: **Ver archivo** abre el resultado en el reproductor por defecto; **Ver carpeta** lo resalta en el explorador.
5. **Otra tarea** limpia el estado para empezar de cero.