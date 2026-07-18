# VideosCortador

App local con interfaz web para **cortar videos sin pérdida de calidad** usando FFmpeg (`-c copy`). Sube un video, elige los puntos de inicio y fin, y genera el corte junto al archivo original.

> Guía detallada de instalación por sistema operativo: [installation.md](installation.md)

## Requisitos

- **Python 3.9+**
- **FFmpeg** (incluye `ffmpeg` y `ffprobe`)

## Instalación rápida

1. **Clonar el repo**
```bash
git clone https://github.com/srllamadev/ZeroLoss-Video-Cutter.git
cd videoscortador
```

2. **Instalar FFmpeg**
- Windows: `winget install Gyan.FFmpeg`
- macOS: `brew install ffmpeg`
- Linux: `sudo apt install -y ffmpeg`

3. **Crear entorno virtual e instalar dependencias**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

python -m pip install -r requirements.txt
```

## Ejecutar

**Windows (doble clic):** abre `iniciar_app.bat`

**Manual (cualquier SO):**
```bash
python app.py
```

Abrir en el navegador: **http://127.0.0.1:8013**

## Uso

1. Arrastra el video o usa **Seleccionar video**.
2. Mueve los sliders o escribe minutos/segundos.
3. Pulsa **Cortar video** → se guarda como `video_cut_1.mp4`, `video_cut_2.mp4`, etc., junto al original.
4. **Ver archivo** abre el resultado · **Ver carpeta** lo resalta en el explorador.