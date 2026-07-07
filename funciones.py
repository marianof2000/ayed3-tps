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
import re
import textwrap


CARPETA_EJERCICIOS: str = "ejercicios"
NOMBRE_MENU: str = "menu.py"
NOMBRE_README: str = "README.md"


CONTENIDO_MENU: str = r'''#!/usr/bin/env python3
"""
Menú automático del Trabajo Práctico.

Este archivo fue generado automáticamente por generar_menus.py.
Detecta los ejercicios actuales del directorio y permite ejecutarlos.
"""

from pathlib import Path
import subprocess
import sys


def _obtener_ejercicios() -> list[Path]:
    """
    Devuelve la lista de archivos de ejercicios del directorio actual.

    Contrato:
    - Busca ejercicios Python en la misma carpeta donde está este menu.py.
    - Considera ejercicios a los archivos Python con formato tp*_ej*.py.

    Precondiciones:
    - El archivo menu.py debe estar dentro del directorio del TP.

    Postcondiciones:
    - Devuelve una lista ordenada de objetos Path.
    - No modifica archivos ni directorios.

    Se consideran ejercicios los archivos que empiezan con 'tp',
    contienen '_ej' y terminan en '.py'.
    """
    carpeta_actual = Path(__file__).parent

    ejercicios = sorted(
        archivo
        for archivo in carpeta_actual.glob("tp*_ej*.py")
        if archivo.is_file()
    )

    return ejercicios


def _mostrar_menu(ejercicios: list[Path]) -> None:
    """
    Muestra por pantalla las opciones disponibles del menú.

    Contrato:
    - Recibe una lista de ejercicios y presenta una opción por ejercicio.
    - Siempre muestra la opción para salir.

    Precondiciones:
    - ejercicios debe ser una lista o iterable de objetos Path.

    Postcondiciones:
    - El menú queda impreso en pantalla.
    - No modifica la lista recibida.
    """
    print()
    print("=" * 60)
    print(f"Menú de ejercicios - {Path(__file__).parent.name}")
    print("=" * 60)

    if not ejercicios:
        print("No se encontraron ejercicios en este directorio.")
        print("Los archivos deben llamarse, por ejemplo: tp01_ej01_nombre.py")
        print()
        print("0. Salir")
        return

    for i, ejercicio in enumerate(ejercicios, start=1):
        print(f"{i}. {ejercicio.stem}")

    print()
    print("T. Ejecutar todos")
    print("0. Salir")


def _ejecutar_archivo(archivo: Path) -> None:
    """
    Ejecuta un archivo de ejercicio individual.

    Contrato:
    - Ejecuta el archivo recibido usando el mismo intérprete de Python.
    - Informa si el archivo termina con errores.

    Precondiciones:
    - archivo debe ser un Path que apunte a un archivo Python existente.

    Postcondiciones:
    - El proceso del ejercicio fue lanzado.
    - El usuario debe presionar ENTER para volver al menú.
    """
    print()
    print("-" * 60)
    print(f"Ejecutando: {archivo.name}")
    print("-" * 60)

    resultado = subprocess.run(
        [sys.executable, str(archivo)],
        cwd=archivo.parent
    )

    if resultado.returncode != 0:
        print()
        print(f"El archivo {archivo.name} terminó con errores.")

    input("\nPresione ENTER para continuar...")


def _ejecutar_todos(ejercicios: list[Path]) -> None:
    """
    Ejecuta todos los ejercicios recibidos.

    Contrato:
    - Recorre la lista de ejercicios y ejecuta cada archivo.
    - Cuenta cuántos terminaron correctamente.

    Precondiciones:
    - ejercicios debe ser una lista o iterable de objetos Path.

    Postcondiciones:
    - Se imprime un resumen con la cantidad de ejecuciones correctas.
    - El usuario debe presionar ENTER para volver al menú.
    """
    if not ejercicios:
        print("No hay ejercicios para ejecutar.")
        input("\nPresione ENTER para continuar...")
        return

    correctos = 0

    for ejercicio in ejercicios:
        print()
        print("=" * 60)
        print(f"Ejecutando: {ejercicio.name}")
        print("=" * 60)

        resultado = subprocess.run(
            [sys.executable, str(ejercicio)],
            cwd=ejercicio.parent
        )

        if resultado.returncode == 0:
            correctos += 1
        else:
            print(f"El archivo {ejercicio.name} terminó con errores.")

    print()
    print("=" * 60)
    print("Resumen")
    print("=" * 60)
    print(f"Ejercicios ejecutados correctamente: {correctos}/{len(ejercicios)}")

    input("\nPresione ENTER para continuar...")


def main() -> None:
    """
    Controla el ciclo principal del menú generado.

    Contrato:
    - Muestra opciones, lee la selección del usuario y ejecuta la acción elegida.
    - Finaliza cuando el usuario ingresa 0.

    Precondiciones:
    - Debe ejecutarse desde un directorio TP con posibles archivos tp*_ej*.py.

    Postcondiciones:
    - El programa termina cuando el usuario elige salir.
    - No altera los archivos de ejercicios.
    """
    while True:
        ejercicios = _obtener_ejercicios()
        _mostrar_menu(ejercicios)

        opcion = input("\nSeleccione una opción: ").strip().lower()

        if opcion == "0":
            print("Fin del programa.")
            break

        if opcion == "t":
            _ejecutar_todos(ejercicios)
            continue

        try:
            numero = int(opcion)

            if 1 <= numero <= len(ejercicios):
                _ejecutar_archivo(ejercicios[numero - 1])
            else:
                print("Opción inválida.")
                input("\nPresione ENTER para continuar...")

        except ValueError:
            print("Opción inválida.")
            input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()
'''


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

    ruta_menu.write_text(
        textwrap.dedent(CONTENIDO_MENU),
        encoding="utf-8"
    )

    try:
        ruta_menu.chmod(ruta_menu.stat().st_mode | 0o111)
    except OSError:
        pass

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

    lineas: list[str] = []

    lineas.append(f"# {titulo}")
    lineas.append("")
    lineas.append("Este directorio contiene los ejercicios correspondientes a este trabajo práctico.")
    lineas.append("")
    lineas.append("> Archivo generado automáticamente por `generar_menus.py`.")
    lineas.append("> Si se agregan, eliminan o renombran ejercicios, ejecutar nuevamente el script maestro.")
    lineas.append("")

    lineas.append("## Archivos incluidos")
    lineas.append("")

    if ejercicios:
        lineas.append("| Nº | Archivo | Ejecución |")
        lineas.append("|---:|---|---|")

        for indice, ejercicio in enumerate(ejercicios, start=1):
            lineas.append(
                f"| {indice} | `{ejercicio.name}` | `python {ejercicio.name}` |"
            )
    else:
        lineas.append("No se encontraron archivos de ejercicios.")
        lineas.append("")
        lineas.append("Los archivos deben nombrarse con el formato:")
        lineas.append("")
        lineas.append("```text")
        lineas.append("tp01_ej01_descripcion.py")
        lineas.append("tp01_ej02_descripcion.py")
        lineas.append("```")

    lineas.append("")
    lineas.append("## Ejecutar un ejercicio")
    lineas.append("")
    lineas.append("Desde este directorio:")
    lineas.append("")
    lineas.append("```bash")
    if ejercicios:
        lineas.append(f"python {ejercicios[0].name}")
    else:
        lineas.append("python tp01_ej01_nombre_del_ejercicio.py")
    lineas.append("```")
    lineas.append("")

    lineas.append("## Ejecutar el menú")
    lineas.append("")
    lineas.append("Desde este directorio:")
    lineas.append("")
    lineas.append("```bash")
    lineas.append("python menu.py")
    lineas.append("```")
    lineas.append("")

    lineas.append("## Ejecutar todos los ejercicios")
    lineas.append("")
    lineas.append("Ingresar al menú:")
    lineas.append("")
    lineas.append("```bash")
    lineas.append("python menu.py")
    lineas.append("```")
    lineas.append("")
    lineas.append("Luego seleccionar la opción:")
    lineas.append("")
    lineas.append("```text")
    lineas.append("T. Ejecutar todos")
    lineas.append("```")
    lineas.append("")

    ruta_readme.write_text("\n".join(lineas), encoding="utf-8")

    return ruta_readme
