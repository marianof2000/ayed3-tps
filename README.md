# Algoritmos y Estructuras de Datos I
## Trabajos Prácticos

Repositorio con la resolución de los trabajos prácticos de la materia **Programación I / Algoritmos y Estructuras de Datos I**.

## Índice

- [Datos del alumno](#datos-del-alumno)
- [Objetivo del repositorio](#objetivo-del-repositorio)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Crear la estructura inicial](#crear-la-estructura-inicial)
- [Actualizar menús y README](#actualizar-menús-y-readme)
- [Criterios generales de programación](#criterios-generales-de-programación)
- [Qué se debe usar](#qué-se-debe-usar)
- [Qué no se debe usar](#qué-no-se-debe-usar)
- [Criterio general](#criterio-general)
- [Clonar y reiniciar Git](#clonar-y-reiniciar-git)
- [Verificar que el remoto sea correcto](#verificar-que-el-remoto-sea-correcto)
- [Importante](#importante)

## Datos del alumno

- **Apellido y nombre:** 
- **Legajo:** 
- **Curso / Comisión:** 
- **Docente:** 
- **Año:** 

## Objetivo del repositorio

Este repositorio tiene como finalidad organizar y documentar las soluciones de los trabajos prácticos de la materia.

Cada trabajo práctico se encuentra separado por tema, con sus respectivos ejercicios resueltos en archivos individuales de Python.

## Estructura del proyecto

```text
ayed1-tps/
│
├── README.md
├── .gitignore
├── crear_estructura.sh
├── crear_estructura.bat
├── generar_menus.py
├── funciones.py
├── contenido_menu.py
│
├── consignas/
│   └── P1_AyED1 - Guia de Trabajos Practicos 2024.pdf
│
├── ejercicios/
│   ├── tp01_funciones/
│   ├── tp02_listas/
│   ├── tp03_matrices/
│   ├── tp04_cadenas/
│   ├── tp05_excepciones/
│   ├── tp06_archivos/
│   ├── tp07_recursividad/
│   └── tp08_tuplas_conjuntos_diccionarios/
│
├── datos/
│   ├── entrada/
│   └── salida/
│
└── tests/
```

## Crear la estructura inicial

El repositorio incluye dos scripts para crear la estructura base del proyecto desde cero:

- `crear_estructura.sh`: para Linux, macOS o terminal Bash.
- `crear_estructura.bat`: para Windows desde CMD o PowerShell.

Ambos scripts crean las carpetas principales (`consignas/`, `ejercicios/`, `datos/`, `tests/`), los directorios de TP del 01 al 08, archivos `.gitkeep`, README iniciales por TP y un `.gitignore` básico.

### Linux, macOS o Bash

Desde la carpeta donde se quiere crear el proyecto:

```bash
chmod +x crear_estructura.sh
./crear_estructura.sh
```

Por defecto crea una carpeta llamada `ayed1-tps`. También se puede indicar otro nombre:

```bash
./crear_estructura.sh mi-proyecto
```

### Windows

Desde CMD o PowerShell, ubicándose en la carpeta donde se quiere crear el proyecto:

```bat
crear_estructura.bat
```

Por defecto crea una carpeta llamada `ayed1-tps`. También se puede indicar otro nombre:

```bat
crear_estructura.bat mi-proyecto
```

Estos scripts están pensados para preparar una estructura inicial. Si se ejecutan sobre una carpeta existente, pueden crear archivos faltantes y actualizar el `.gitignore` de esa estructura.

## Actualizar menús y README

Cada vez que se agreguen, eliminen o renombren ejercicios, ejecutar desde la raíz del proyecto:

En Linux, macOS o Bash:

```bash
python3 generar_menus.py
```

En Windows:

```powershell
python generar_menus.py
```

Si el comando `python` no está disponible en Windows, usar:

```powershell
py generar_menus.py
```

Ese comando actualiza automáticamente el `README.md` y el `menu.py` de cada directorio dentro de `ejercicios/`.

La generación está separada en tres archivos:

* `generar_menus.py`: punto de entrada que recorre los directorios de trabajos prácticos.
* `funciones.py`: funciones auxiliares para buscar directorios y generar archivos.
* `contenido_menu.py`: plantilla estática del `menu.py` generado automáticamente.

## Criterios generales de programación

Las soluciones de este repositorio deben respetar criterios comunes de organización, legibilidad y buenas prácticas de programación en Python.

El objetivo no es solamente que el programa funcione, sino que el código sea claro, verificable y fácil de corregir.

---

## Qué se debe usar

### Organización de archivos

Cada ejercicio debe resolverse en un archivo independiente, ubicado dentro de la carpeta correspondiente al trabajo práctico.

El nombre del archivo debe respetar el siguiente formato:

```text
tpXX_ejYY_nombre_descriptivo.py
```

Ejemplos:

```text
tp02_ej01_operaciones_lista.py
tp03_ej05_cine.py
tp04_ej14_validar_email.py
```

Donde:

* `tpXX` indica el número de trabajo práctico.
* `ejYY` indica el número de ejercicio.
* `nombre_descriptivo` resume brevemente el contenido del ejercicio.
* El nombre del archivo debe escribirse en minúsculas, sin tildes y con guiones bajos.

---

### Estructura interna de cada archivo

Cada archivo debe tener, como mínimo, la siguiente estructura:

```python
# TPXX - Ejercicio YY
# Descripción breve del ejercicio


def _funcion_auxiliar() -> None:
    """
    Contrato:
        Describe qué hace la función.

    Precondiciones:
        Indica qué condiciones deben cumplirse antes de ejecutar la función.

    Postcondiciones:
        Indica qué resultado produce o qué modifica la función.
    """
    ...


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """
    ...


if __name__ == "__main__":
    main()
```

---

### Funciones

Todas las funciones auxiliares deben comenzar con guion bajo `_`.

Ejemplos:

```python
def _generar_lista() -> list[int]:
    ...


def _mostrar_matriz(matriz: list[list[int]]) -> None:
    ...


def _validar_entero(mensaje: str) -> int:
    ...
```

La única función que no debe comenzar con guion bajo es:

```python
def main() -> None:
    ...
```

---

### Contrato, precondiciones y postcondiciones

Toda función debe incluir un `docstring` con:

* contrato;
* precondiciones;
* postcondiciones.

Ejemplo:

```python
def _calcular_promedio(numeros: list[int]) -> float:
    """
    Contrato:
        Calcula el promedio de una lista de números enteros.

    Precondiciones:
        La lista debe contener al menos un elemento.

    Postcondiciones:
        Devuelve el promedio como número real.
    """
    return sum(numeros) / len(numeros)
```

---

### Type hints

Todas las funciones deben usar anotaciones de tipo.

Ejemplos:

```python
def _es_par(numero: int) -> bool:
    ...


def _normalizar(lista: list[int]) -> list[float]:
    ...


def _buscar_valor(matriz: list[list[int]], valor: int) -> tuple[int, int] | None:
    ...


def main() -> None:
    ...
```

---

### Texto visible para el usuario

Todo texto mostrado por pantalla debe estar en español y con tildes correctas.

Ejemplos correctos:

```python
print("La matriz es simétrica.")
print("Ingrese un número entero:")
print("Opción inválida.")
```

Ejemplos incorrectos:

```python
print("La matriz es simetrica.")
print("Ingrese un numero entero:")
print("Opcion invalida.")
```

---

### Librerías permitidas

Se pueden usar solamente las siguientes librerías, cuando sean necesarias:

```python
import random
import json
import os
from typing import ...
```

También se permite usar `tabulate` si mejora la presentación de los datos:

```python
from tabulate import tabulate
```

Si se usa `tabulate`, el programa debería seguir siendo comprensible aunque la tabla se imprima de forma simple.

---

### Recursos de Python permitidos

Se permite usar recursos propios del lenguaje Python cuando ayuden a escribir soluciones claras:

* listas;
* tuplas;
* conjuntos (`set`);
* diccionarios;
* listas por comprensión;
* conjuntos por comprensión;
* diccionarios por comprensión;
* funciones `lambda`;
* funciones de orden superior como `map()`, `filter()`, `any()` y `all()`;
* generadores;
* decoradores, si tienen una finalidad clara;
* slices o rebanadas;
* funciones built-in como `len()`, `range()`, `enumerate()`, `zip()`, `sum()`, `min()`, `max()`, `sorted()` y `reversed()`.

Ejemplos:

```python
cuadrados = [numero ** 2 for numero in range(1, 11)]

impares = list(filter(lambda numero: numero % 2 != 0, numeros))

conteo = {valor: lista.count(valor) for valor in lista}

pares = {numero for numero in numeros if numero % 2 == 0}
```

---

### Validación de entradas

Cuando se pidan datos al usuario, se deben validar las entradas.

Ejemplo recomendado:

```python
def _ingresar_entero(mensaje: str) -> int:
    """
    Contrato:
        Solicita un número entero al usuario.

    Precondiciones:
        El mensaje debe ser una cadena de caracteres.

    Postcondiciones:
        Devuelve un número entero válido ingresado por teclado.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número entero.")
```

Se recomienda usar `while True` cuando simplifique la validación o los menús interactivos.

---

### Criterios de calidad

Las soluciones deben priorizar:

* claridad;
* legibilidad;
* separación entre lógica e interacción con el usuario;
* funciones pequeñas;
* reutilización de código;
* criterio DRY, es decir, evitar repetir innecesariamente la misma lógica;
* nombres descriptivos;
* validación de datos;
* mensajes claros por pantalla;
* respeto estricto de la consigna.

---

## Qué no se debe usar

### No usar librerías externas no autorizadas

No se deben usar librerías como:

```text
numpy
pandas
matplotlib
scipy
collections
```

salvo autorización expresa del docente o indicación específica de la consigna.

---

### No usar programación orientada a objetos

No usar clases.

Ejemplo no permitido:

```python
class Alumno:
    ...
```

Los ejercicios deben resolverse con funciones y estructuras básicas de Python.

---

### No usar arquitecturas innecesarias

No crear paquetes, módulos adicionales o estructuras complejas si el ejercicio puede resolverse en un único archivo.

No crear archivos auxiliares innecesarios.

---

### No modificar archivos automáticos

No modificar manualmente archivos generados automáticamente dentro de cada carpeta de TP, como:

```text
menu.py
README.md
```

Cuando se agreguen, eliminen o renombren ejercicios, se debe volver a ejecutar el script correspondiente para actualizar esos archivos.

---

### No ignorar restricciones de la consigna

Si la consigna indica una restricción específica, debe respetarse aunque Python ofrezca una forma más corta de resolverlo.

Ejemplos:

* Si la consigna dice “sin usar listas auxiliares”, no se deben crear listas auxiliares.
* Si la consigna dice “sin usar rebanadas”, no se deben usar slices.
* Si la consigna dice “modificar la lista original”, no alcanza con devolver una copia modificada.
* Si la consigna pide usar `filter()`, debe usarse `filter()`.
* Si la consigna pide usar listas por comprensión, debe usarse comprensión de listas.

---

### No usar atajos que oculten el razonamiento

No se deben usar soluciones excesivamente compactas si dificultan entender el algoritmo.

Ejemplo poco recomendable para una primera lectura:

```python
resultado = all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))
```

Ejemplo más explícito:

```python
ordenada = True

for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        ordenada = False
```

---

### No usar variables globales para el estado principal

Evitar este tipo de código:

```python
lista = []


def cargar() -> None:
    lista.append(10)
```

Preferir pasar los datos como parámetros y devolver resultados.

Ejemplo recomendado:

```python
def _agregar_valor(lista: list[int], valor: int) -> None:
    lista.append(valor)
```

---

### No subir archivos innecesarios al repositorio

No subir:

```text
__pycache__/
*.pyc

.venv/
venv/
env/

.vscode/
.idea/

*.log
*.pdf

.python-version
```

Estos archivos deben quedar excluidos mediante `.gitignore` (usarlo de ejemplo).

---

## Criterio general

Cada ejercicio debe poder ejecutarse de forma independiente y debe mostrar resultados suficientes para comprobar su funcionamiento.

El código debe ser correcto, claro, mantenible y respetuoso de las restricciones particulares de cada consigna.

## Clonar y reiniciar Git

Si no se usa la opción **Use this template** de GitHub, se puede clonar este repositorio y eliminar el historial de Git para comenzar un repositorio propio desde cero.

Esta opción permite conservar la estructura de carpetas y archivos, pero descartar el historial del repositorio original.

---

### En Linux o macOS

```bash
git clone https://github.com/marianof2000/ayed1-tps apellido_nombre_ayed1_tps
cd apellido_nombre_ayed1_tps

rm -rf .git

git init
git add .
git commit -m "Estructura inicial de trabajos prácticos"
```

Luego crear un repositorio vacío en GitHub y asociarlo:

```bash
git remote add origin https://github.com/usuario/apellido_nombre_ayed1_tps.git
git branch -M main
git push -u origin main
```

---

### En Windows PowerShell

```powershell
git clone https://github.com/marianof2000/ayed1-tps apellido_nombre_ayed1_tps
cd apellido_nombre_ayed1_tps

Remove-Item -Recurse -Force .git

git init
git add .
git commit -m "Estructura inicial de trabajos prácticos"
```

Luego crear un repositorio vacío en GitHub y asociarlo:

```powershell
git remote add origin https://github.com/usuario/apellido_nombre_ayed1_tps.git
git branch -M main
git push -u origin main
```

---

## Verificar que el remoto sea correcto

Antes de empezar a trabajar, verificar que el repositorio local apunte al repositorio propio del alumno:

```bash
git remote -v
```

La salida debe mostrar una URL correspondiente al repositorio propio, por ejemplo:

```text
origin  https://github.com/usuario/apellido_nombre_ayed1_tps.git (fetch)
origin  https://github.com/usuario/apellido_nombre_ayed1_tps.git (push)
```

Si aparece la URL del repositorio original, se debe corregir el remoto:

```bash
git remote set-url origin https://github.com/usuario/apellido_nombre_ayed1_tps.git
```

---

## Importante

No se debe trabajar directamente sobre el repositorio original de la cátedra o plantilla.

Cada alumno debe tener su propio repositorio, con su propio historial de commits.
