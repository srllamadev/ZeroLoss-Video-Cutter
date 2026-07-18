@echo off
REM ============================================================
REM  ZeroLoss-Video-Cutter - Lanzador automatico (doble clic)
REM  Verifica FFmpeg, crea/activa venv, instala deps, arranca
REM  el servidor Flask y abre el navegador por defecto.
REM ============================================================
title ZeroLoss-Video-Cutter - Servidor local
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ===================================================
echo   ZeroLoss-Video-Cutter :: Iniciando aplicacion local
echo ===================================================
echo.

REM ------------------------------------------------------------
REM 1. Verificacion de FFmpeg en el PATH del sistema
REM ------------------------------------------------------------
echo [1/5] Verificando FFmpeg...
where ffmpeg >nul 2>nul
if errorlevel 1 (
    echo.
    echo [ERROR] No se encontro FFmpeg en el sistema.
    echo         FFmpeg es obligatorio para el corte de videos.
    echo.
    echo         Instalalo con:
    echo             winget install Gyan.FFmpeg
    echo.
    echo         O descargalo desde https://www.gyan.dev/ffmpeg/builds/
    echo         y agrega la carpeta "bin" al PATH.
    echo.
    pause
    exit /b 1
)
echo       FFmpeg OK.
echo.

REM ------------------------------------------------------------
REM 2. Verificacion de Python
REM ------------------------------------------------------------
echo [2/5] Verificando Python...
python --version >nul 2>nul
if errorlevel 1 (
    echo.
    echo [ERROR] No se encontro Python en el sistema.
    echo         Instalalo desde https://www.python.org/downloads/
    echo         ^(marca "Add Python to PATH" durante la instalacion^).
    echo.
    pause
    exit /b 1
)
echo       Python OK.
echo.

REM ------------------------------------------------------------
REM 3. Entorno virtual: crear si no existe
REM ------------------------------------------------------------
if not exist "venv\Scripts\activate.bat" (
    echo [3/5] Creando entorno virtual en "venv\"...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
    echo       Entorno virtual creado.
) else (
    echo [3/5] Entorno virtual ya existe. Reutilizando.
)
echo.

REM ------------------------------------------------------------
REM 4. Activar venv e instalar dependencias
REM ------------------------------------------------------------
echo [4/5] Activando entorno virtual...
call venv\Scripts\activate.bat
echo       Instalando dependencias (silencioso)...
python -m pip install --quiet --upgrade pip >nul 2>nul
python -m pip install --quiet -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Fallo la instalacion de dependencias.
    pause
    exit /b 1
)
echo       Dependencias listas.
echo.

REM ------------------------------------------------------------
REM 5. Abrir navegador y arrancar el servidor Flask
REM ------------------------------------------------------------
echo [5/5] Arrancando servidor Flask en http://127.0.0.1:8013 ...

REM Abre el navegador despues de 2 segundos sin bloquear la consola
start "" /b cmd /c "timeout /t 2 /nobreak >nul && start """" http://127.0.0.1:8013"

echo.
echo ===================================================
echo   Servidor activo. NO cierres esta ventana.
echo   Logs en vivo ↓
echo ===================================================
echo.

REM Mantiene la consola abierta mostrando los logs del servidor
python app.py

REM Si la ejecucion llega aqui (el servidor cerro), pausar
echo.
echo [INFO] El servidor se detuvo.
pause