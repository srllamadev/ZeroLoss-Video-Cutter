# Instalación

Guía directa para desplegar **ZeroLoss-Video-Cutter** localmente. Requisito común: **Python 3.9+** y **FFmpeg** (incluye `ffmpeg` y `ffprobe`).

---

## Windows

### 1. Instalar Python
Descarga desde https://www.python.org/downloads/ y durante la instalación marca **"Add Python to PATH"**.

### 2. Instalar FFmpeg
```bat
winget install Gyan.FFmpeg
```
O descarga desde https://www.gyan.dev/ffmpeg/builds/, extrae y agrega la carpeta `bin` al PATH.

### 3. Clonar el repo
```bat
git clone https://github.com/srllamadev/ZeroLoss-Video-Cutter.git
cd ZeroLoss-Video-Cutter
```

### 4. Crear entorno virtual e instalar dependencias
```bat
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

### 5. Ejecutar
Opción A — con el lanzador (doble clic):
```bat
iniciar_app.bat
```
Opción B — manual:
```bat
venv\Scripts\activate
python app.py
```

Abrir: **http://127.0.0.1:8013**

---

## Linux (Debian/Ubuntu)

### 1. Instalar Python
```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip
```

### 2. Instalar FFmpeg
```bash
sudo apt install -y ffmpeg
```

### 3. Clonar el repo
```bash
git clone https://github.com/srllamadev/ZeroLoss-Video-Cutter.git
cd ZeroLoss-Video-Cutter
```

### 4. Crear entorno virtual e instalar dependencias
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### 5. Ejecutar
```bash
python app.py
```

Abrir: **http://127.0.0.1:8013**

---

## macOS

### 1. Instalar Python
```bash
brew install python
```
O descarga desde https://www.python.org/downloads/

### 2. Instalar FFmpeg
```bash
brew install ffmpeg
```

### 3. Clonar el repo
```bash
git clone https://github.com/srllamadev/ZeroLoss-Video-Cutter.git
cd ZeroLoss-Video-Cutter
```

### 4. Crear entorno virtual e instalar dependencias
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### 5. Ejecutar
```bash
python app.py
```

Abrir: **http://127.0.0.1:8013**

---

## Verificación de dependencias

Comprueba que todo está listo antes de ejecutar:
```bash
python --version
ffmpeg -version
ffprobe -version
```