#!/usr/bin/env bash

set -euo pipefail

PROYECTO="${1:-ayed1-tps}"

mkdir -p "$PROYECTO"/{consignas,ejercicios,datos/{entrada,salida},tests}

mkdir -p "$PROYECTO"/ejercicios/{\
tp01_funciones,\
tp02_listas,\
tp03_matrices,\
tp04_cadenas,\
tp05_excepciones,\
tp06_archivos,\
tp07_recursividad,\
tp08_tuplas_conjuntos_diccionarios\
}

touch "$PROYECTO/README.md"
touch "$PROYECTO/.gitignore"

touch "$PROYECTO/consignas/.gitkeep"
touch "$PROYECTO/datos/entrada/.gitkeep"
touch "$PROYECTO/datos/salida/.gitkeep"
touch "$PROYECTO/tests/.gitkeep"

for tp in "$PROYECTO"/ejercicios/tp*/; do
    touch "${tp}README.md"
done

cat > "$PROYECTO/.gitignore" <<'EOF'
__pycache__/
*.pyc

.venv/
venv/
env/

.vscode/
.idea/

*.log

datos/salida/*
!datos/salida/.gitkeep
EOF

echo "Estructura creada en: $PROYECTO"