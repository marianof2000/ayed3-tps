@echo off
setlocal

set "PROYECTO=%~1"
if "%PROYECTO%"=="" set "PROYECTO=ayed1-tps"

mkdir "%PROYECTO%\consignas" 2>nul
mkdir "%PROYECTO%\ejercicios" 2>nul
mkdir "%PROYECTO%\datos\entrada" 2>nul
mkdir "%PROYECTO%\datos\salida" 2>nul
mkdir "%PROYECTO%\tests" 2>nul

mkdir "%PROYECTO%\ejercicios\tp01_funciones" 2>nul
mkdir "%PROYECTO%\ejercicios\tp02_listas" 2>nul
mkdir "%PROYECTO%\ejercicios\tp03_matrices" 2>nul
mkdir "%PROYECTO%\ejercicios\tp04_cadenas" 2>nul
mkdir "%PROYECTO%\ejercicios\tp05_excepciones" 2>nul
mkdir "%PROYECTO%\ejercicios\tp06_archivos" 2>nul
mkdir "%PROYECTO%\ejercicios\tp07_recursividad" 2>nul
mkdir "%PROYECTO%\ejercicios\tp08_tuplas_conjuntos_diccionarios" 2>nul

type nul > "%PROYECTO%\README.md"
type nul > "%PROYECTO%\consignas\.gitkeep"
type nul > "%PROYECTO%\datos\entrada\.gitkeep"
type nul > "%PROYECTO%\datos\salida\.gitkeep"
type nul > "%PROYECTO%\tests\.gitkeep"

type nul > "%PROYECTO%\ejercicios\tp01_funciones\README.md"
type nul > "%PROYECTO%\ejercicios\tp02_listas\README.md"
type nul > "%PROYECTO%\ejercicios\tp03_matrices\README.md"
type nul > "%PROYECTO%\ejercicios\tp04_cadenas\README.md"
type nul > "%PROYECTO%\ejercicios\tp05_excepciones\README.md"
type nul > "%PROYECTO%\ejercicios\tp06_archivos\README.md"
type nul > "%PROYECTO%\ejercicios\tp07_recursividad\README.md"
type nul > "%PROYECTO%\ejercicios\tp08_tuplas_conjuntos_diccionarios\README.md"

(
echo __pycache__/
echo *.pyc
echo.
echo .venv/
echo venv/
echo env/
echo.
echo .vscode/
echo .idea/
echo.
echo *.log
echo.
echo datos/salida/*
echo !datos/salida/.gitkeep
) > "%PROYECTO%\.gitignore"

echo Estructura creada en: %PROYECTO%

endlocal
