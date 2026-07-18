# Installation

A straightforward guide to deploy **ZeroLoss-Video-Cutter** locally. General requirements: **Python 3.9+** and **FFmpeg** (including `ffmpeg` and `ffprobe`).

---

## Windows

### 1. Install Python

Download it from https://www.python.org/downloads/ and make sure to select **"Add Python to PATH"** during installation.

### 2. Install FFmpeg

```bat
winget install Gyan.FFmpeg
```

Alternatively, download it from https://www.gyan.dev/ffmpeg/builds/, extract the files, and add the `bin` folder to the system PATH.

### 3. Clone the Repository

```bat
git clone https://github.com/srllamadev/ZeroLoss-Video-Cutter.git
cd ZeroLoss-Video-Cutter
```

### 4. Create a Virtual Environment and Install Dependencies

```bat
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

### 5. Run the Application

Option A — using the launcher by double-clicking it:

```bat
iniciar_app.bat
```

Option B — run it manually:

```bat
venv\Scripts\activate
python app.py
```

Open: **http://127.0.0.1:8013**

---

## Linux (Debian/Ubuntu)

### 1. Install Python

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip
```

### 2. Install FFmpeg

```bash
sudo apt install -y ffmpeg
```

### 3. Clone the Repository

```bash
git clone https://github.com/srllamadev/ZeroLoss-Video-Cutter.git
cd ZeroLoss-Video-Cutter
```

### 4. Create a Virtual Environment and Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Open: **http://127.0.0.1:8013**

---

## macOS

### 1. Install Python

```bash
brew install python
```

Alternatively, download it from https://www.python.org/downloads/

### 2. Install FFmpeg

```bash
brew install ffmpeg
```

### 3. Clone the Repository

```bash
git clone https://github.com/srllamadev/ZeroLoss-Video-Cutter.git
cd ZeroLoss-Video-Cutter
```

### 4. Create a Virtual Environment and Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Open: **http://127.0.0.1:8013**

---

## Dependency Verification

Check that everything is properly installed before running the application:

```bash
python --version
ffmpeg -version
ffprobe -version
```
