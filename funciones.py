"""
Funciones auxiliares para generar menús y README de trabajos prácticos.

Contrato:
- Provee operaciones reutilizables para buscar directorios TP.
- Genera archivos menu.py y README.md dentro de cada directorio.
- Mantiene separados los detalles de generación del punto de entrada.

Precondiciones generales:
- Las rutas recibidas deben ser objetos compatibles con pathlib.Path.
- El proyecto debe usar la carpeta ejercicios/ para agrupar los TP.

Postcondiciones generales:
- Las funciones de generación devuelven la ruta del archivo creado o actualizado.
- No se modifican archivos fuera del directorio TP recibido.
"""

from pathlib import Path
import os
import re
import stat

from contenido_menu import CONTENIDO_MENU

CARPETA_EJERCICIOS: str = "ejercicios"
NOMBRE_MENU: str = "menu.py"
NOMBRE_README: str = "README.md"


def _formatear_titulo_tp(nombre_directorio: str) -> str:
    """
    Contrato:
    - Convierte el nombre de un directorio TP en un título legible.
    - Preserva el número de TP en mayúsculas.

    Precondiciones:
    - nombre_directorio debe ser una cadena no vacía.

    Postcondiciones:
    - Devuelve una cadena formateada para usar como título.
    - No modifica archivos ni depende del sistema de archivos.

    Convierte nombres como:
    tp01_funciones
    tp08_tuplas_conjuntos_diccionarios

    en:
    TP01 - Funciones
    TP08 - Tuplas Conjuntos Diccionarios
    """
    coincidencia = re.match(r"(tp\d+)_?(.*)", nombre_directorio, re.IGNORECASE)

    if not coincidencia:
        return nombre_directorio.replace("_", " ").title()

    numero_tp = coincidencia.group(1).upper()
    tema = coincidencia.group(2).replace("_", " ").title()

    if tema:
        return f"{numero_tp} - {tema}"

    return numero_tp


def _obtener_ejercicios(directorio_tp: Path) -> list[Path]:
    """
    Devuelve una lista ordenada de archivos tp*_ej*.py dentro de un directorio TP.

    Contrato:
    - Busca archivos de ejercicios dentro del directorio recibido.

    Precondiciones:
    - directorio_tp debe ser un Path que apunte a un directorio existente.

    Postcondiciones:
    - Devuelve una lista ordenada de objetos Path.
    - No modifica el contenido del directorio.
    """
    return sorted(
        archivo
        for archivo in directorio_tp.glob("tp*_ej*.py")
        if archivo.is_file()
    )


def _marcar_como_ejecutable_si_corresponde(ruta_archivo: Path) -> None:
    """
    Intenta marcar un archivo como ejecutable en sistemas compatibles.

    Contrato:
    - Agrega permisos de ejecución en Linux, macOS y otros sistemas POSIX.
    - En Windows no modifica permisos porque el bit ejecutable POSIX no aplica.

    Precondiciones:
    - ruta_archivo debe ser un Path que apunte a un archivo existente.

    Postcondiciones:
    - Si el sistema lo permite, el archivo queda marcado como ejecutable.
    - Si el sistema no lo permite, no interrumpe la generación del archivo.
    """
    if os.name == "nt":
        return

    permisos_actuales = ruta_archivo.stat().st_mode
    permisos_ejecucion = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH

    try:
        ruta_archivo.chmod(permisos_actuales | permisos_ejecucion)
    except OSError:
        return


def buscar_directorios_tp(raiz: Path) -> list[Path]:
    """
    Busca todos los directorios TP dentro de la carpeta ejercicios/.

    Contrato:
    - Localiza directorios cuyo nombre empieza con tp dentro de ejercicios/.

    Precondiciones:
    - raiz debe ser un Path que apunte a la raíz del proyecto.
    - raiz debe contener la carpeta ejercicios/.

    Postcondiciones:
    - Devuelve una lista ordenada de directorios TP.
    - Lanza FileNotFoundError si no existe ejercicios/.
    """
    carpeta_ejercicios = raiz / CARPETA_EJERCICIOS

    if not carpeta_ejercicios.exists():
        raise FileNotFoundError(
            f"No se encontró la carpeta '{CARPETA_EJERCICIOS}'. "
            f"Ejecutá este script desde la raíz del proyecto."
        )

    directorios_tp = sorted(
        directorio
        for directorio in carpeta_ejercicios.iterdir()
        if directorio.is_dir() and directorio.name.lower().startswith("tp")
    )

    return directorios_tp


def generar_menu_en_directorio(directorio_tp: Path) -> Path:
    """
    Crea o actualiza el archivo menu.py dentro del directorio TP.

    Contrato:
    - Escribe el contenido estándar del menú automático.
    - Intenta dejar el archivo como ejecutable.

    Precondiciones:
    - directorio_tp debe ser un Path que apunte a un directorio existente.
    - El proceso debe tener permisos de escritura en ese directorio.

    Postcondiciones:
    - Devuelve la ruta del menu.py creado o actualizado.
    - El archivo queda escrito con codificación UTF-8.
    """
    ruta_menu = directorio_tp / NOMBRE_MENU

    ruta_menu.write_text(CONTENIDO_MENU, encoding="utf-8")
    _marcar_como_ejecutable_si_corresponde(ruta_menu)

    return ruta_menu


def generar_readme_en_directorio(directorio_tp: Path) -> Path:
    """
    Crea o actualiza el README.md dentro del directorio TP.

    Contrato:
    - Genera documentación del TP con los ejercicios encontrados.
    - Incluye instrucciones para ejecutar ejercicios y el menú.

    Precondiciones:
    - directorio_tp debe ser un Path que apunte a un directorio existente.
    - El proceso debe tener permisos de escritura en ese directorio.

    Postcondiciones:
    - Devuelve la ruta del README.md creado o actualizado.
    - El README queda escrito con codificación UTF-8.
    """
    ruta_readme = directorio_tp / NOMBRE_README
    ejercicios = _obtener_ejercicios(directorio_tp)
    titulo = _formatear_titulo_tp(directorio_tp.name)

    lineas: list[str] = [
        f"# {titulo}",
        "",
        "Este directorio contiene los ejercicios correspondientes a este trabajo práctico.",
        "",
        "> Archivo generado automáticamente por `generar_menus.py`.",
        "> Si se agregan, eliminan o renombran ejercicios, ejecutar nuevamente el script maestro.",
        "",
        "## Archivos incluidos",
        "",
    ]

    if ejercicios:
        lineas.extend([
            "| Nº | Archivo | Ejecución |",
            "|---:|---|---|",
        ])

        lineas.extend(
            f"| {indice} | `{ejercicio.name}` | `python {ejercicio.name}` |"
            for indice, ejercicio in enumerate(ejercicios, start=1)
        )
    else:
        lineas.extend([
            "No se encontraron archivos de ejercicios.",
            "",
            "Los archivos deben nombrarse con el formato:",
            "",
            "```text",
            "tp01_ej01_descripcion.py",
            "tp01_ej02_descripcion.py",
            "```",
        ])

    lineas.extend([
        "",
        "## Ejecutar un ejercicio",
        "",
        "Desde este directorio:",
        "",
        "```bash",
    ])
    if ejercicios:
        lineas.append(f"python {ejercicios[0].name}")
    else:
        lineas.append("python tp01_ej01_nombre_del_ejercicio.py")
    lineas.extend([
        "```",
        "",
        "## Ejecutar el menú",
        "",
        "Desde este directorio:",
        "",
        "```bash",
        "python menu.py",
        "```",
        "",
        "## Ejecutar todos los ejercicios",
        "",
        "Ingresar al menú:",
        "",
        "```bash",
        "python menu.py",
        "```",
        "",
        "Luego seleccionar la opción:",
        "",
        "```text",
        "T. Ejecutar todos",
        "```",
        "",
    ])

    ruta_readme.write_text("\n".join(lineas), encoding="utf-8")

    return ruta_readme
