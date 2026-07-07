"""
Punto de entrada del generador de menús y README.

Contrato:
- Coordina la generación de archivos auxiliares para cada trabajo práctico.
- No contiene la lógica de generación; delega ese trabajo en funciones.py.

Precondiciones:
- El script debe ejecutarse desde la raíz del proyecto.
- Debe existir una carpeta llamada ejercicios/.

Postcondiciones:
- Cada directorio TP encontrado queda procesado por las funciones de generación.
- Se informa por pantalla el resultado del proceso.
"""

from pathlib import Path

from funciones import (
    buscar_directorios_tp,
    generar_menu_en_directorio,
    generar_readme_en_directorio,
)


def main() -> None:
    """
    Ejecuta el proceso principal de generación.

    Contrato:
    - Busca los directorios de trabajos prácticos.
    - Genera o actualiza menu.py y README.md en cada uno.
    - Muestra un resumen del proceso.

    Precondiciones:
    - La carpeta de trabajo actual debe ser la raíz del proyecto.
    - La raíz debe contener la carpeta ejercicios/.

    Postcondiciones:
    - Si hay directorios TP, cada uno tendrá menu.py y README.md actualizados.
    - Si no hay directorios TP, se informa la situación sin generar archivos.
    """
    raiz = Path.cwd()

    print("Generando menús y README de trabajos prácticos...")
    print(f"Raíz del proyecto: {raiz}")
    print()

    directorios_tp = buscar_directorios_tp(raiz)

    if not directorios_tp:
        print("No se encontraron directorios TP dentro de la carpeta ejercicios.")
        return

    for directorio_tp in directorios_tp:
        ruta_menu = generar_menu_en_directorio(directorio_tp)
        ruta_readme = generar_readme_en_directorio(directorio_tp)

        print(f"Directorio: {directorio_tp}")
        print(f"  Actualizado: {ruta_menu.name}")
        print(f"  Actualizado: {ruta_readme.name}")
        print()

    print("Proceso finalizado.")
    print(f"Directorios TP actualizados: {len(directorios_tp)}")


if __name__ == "__main__":
    main()
