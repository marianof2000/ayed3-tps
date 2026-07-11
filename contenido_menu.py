"""
Contenido estático del menu.py generado para cada trabajo práctico.

Este módulo mantiene separada la plantilla del menú para evitar cambios
accidentales dentro de la lógica de generación.
"""

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
