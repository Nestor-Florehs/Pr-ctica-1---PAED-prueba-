# Práctica 1 Programación Avanzada y Estructura de Datos.

## Archivos Principales

### Algoritmos de Ordenamiento
1. **`InsertionSort.py`**: Implementa el algoritmo de Insertion Sort para ordenar listas de diccionarios respecto el nombre de la tarea.
2. **`SelectionSort.py`**: Implementa el algoritmo de Selection Sort para ordenar listas de diccionarios  respecto el nombre de la tarea.
3. **`MergeSort.py`**: Implementa el algoritmo de Merge Sort.
4. **`QuickSort.py`**: Implementa el algoritmo de Quick Sort.

### Otros Archivos
1. **`weightCalculation.py`**: Calcula el peso de cada tarea respecto a su importancia, representada como un color, su fecha de entrega y lo avanzada que está la tarea .
2. **`ExtractData.py`**: Extrae datos de archivos seleccionados y los transforma en listas de diccionarios.
3. **`SortData.py`**: Muestra ejemplos prácticos del uso de los algoritmos de ordenamiento.
4. **`GenerateGrafic.py`**: Genera gráficos de comparación de tiempos de ejecución para los algoritmos.

## Explicación módulos:

### Ordenamiento de listas
- Los algoritmos se pueden aplicar a listas de diccionarios ordenándolos por claves como `name` o `weight`, para ordenar con los algoritmos de ordenación recursivos usaremos la clave `weight` y para los algoritmos imperativos usaremos la clave `name`.

### Cálculo de pesos
- Funciones para calcular pesos de cada tarea basados en parámetros como fecha límite, color en formato hexadecimal y porcentaje de progreso.

### Visualización gráfica
- Uso de `matplotlib` para mostrar visualizaciones del desempeño de los algoritmos y complejidades teóricas.

### Interactividad
- Uso de `tkinter` para seleccionar archivos que contienen los datos a procesar.

## Ejecución

### Ejecución de Pruebas
- Cada script contiene funciones de prueba comentadas que se pueden habilitar para ejecutar ejemplos rápidos.
- Por ejemplo: 
```python
import matplotlib as plt
from GenerateGrafic import measure_recursive_sort_times

def recursive_algorithm_graph():
    # Tamaños de las iteraciones.
    # Si quieres graficar para diferentes tamaños de input modifica la lista.
    sizes = [1, 100, 1000, 5000, 10000, 25000, 50000, 100000, 175000, 250000, 325000, 500000]


    merge_times, quick_times = measure_recursive_sort_times(sizes)

    # Uso de la librería matplotlib para graficar los resultados.
    plt.figure(figsize=(10, 6))

    # Para el eje x utilizamos la lista sizes, haciendole un slicing de la longitud tanto de Merge como de Quick Sort.
    # Para el eje y utilizamos la lista de tiempos de cada uno de los algoritmos.
    plt.plot(sizes[:len(merge_times)], merge_times, label='Merge Sort', marker='o')
    plt.plot(sizes[:len(quick_times)], quick_times, label='Quick Sort', marker='o')

    plt.xlabel("Size of Array (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs. Array Size for Merge Sort and Quick Sort (Up to 500,000 Elements)")
    plt.xscale('log')  
    plt.legend()
    plt.grid(True)
    plt.show()
```
Si quieres probar la función puedes cambiar el valor de sizes para elegir los elemntos que se van a comprobar.


## Instalación y Configuración

Sigue estos pasos para clonar, configurar y ejecutar el proyecto en tu entorno local:

1. **Clonar el repositorio**
   ```bash
   git clone https://git-eng.salleurl.edu/paed-2425/s1-gi-g34/practica-1-grup-34.git
   cd <NOMBRE_DEL_PROYECTO>
   ```
   
## Requisitos Previos

Para ejecutar este programa, asegúrate de tener lo siguiente:

1. **Python 3.12.6**: Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. **Pip 24.3.1**: Tienes que tener instalado el gestor de paquetes de Python.
2. **PyCharm** (opcional, recomendado para desarrollo): Puedes descargar la versión Community o Professional desde [JetBrains](https://www.jetbrains.com/pycharm/).
3. **Matplotlib**: Para ejecutar el código para generar los gráficos necesitaremos la librería matplotlib.

# Instalación de Matplotlib

El proyecto utiliza la biblioteca `matplotlib` para la generación de gráficos y visualizaciones. Sigue las instrucciones a continuación para instalarla.

## Requisitos Previos

Asegúrate de tener instalado Python (versión 3.12.6 o superior es recomendada). Puedes verificar tu versión de Python ejecutando el siguiente comando en tu terminal o consola:
```bash
python --version
```

Asegúrate de tener el gestor de paquetes de Python pip:
```bash
pip --version
```
Si no te enseña la version de pip prueba con ejecutar el siguiente comando en la consola de comandos:
```bash
python -m pip --version
```
Si de esta forma si te muestra tu versión de pip puede ser debido a no tener pip en el PATH del sistema.

## Instalación de Matplotlib

Ejecuta el siguiente comando en la consola de comando.

```bash
cd <path_proyecto>
pip install matplotlib 
```
En su defecto.
```bash 
  cd <path_proyecto>
  python -m pip install matplotlib
```

## Ejecutar el Programa

Para ejecutar el programa en PyCharm:

1. **Abrir el proyecto en PyCharm**
   - Abre PyCharm.
   - Selecciona `Open` y navega hasta el directorio del proyecto.

2. **Configurar el intérprete de Python**
   - Ve a `File > Settings > Project: <NOMBRE_DEL_PROYECTO> > Python Interpreter`.
   - Selecciona Python 3.12.6 como el intérprete del proyecto o apunta al intérprete de tu entorno virtual.

3. **Ejecutar el programa**
   - Abre el archivo principal del programa.
   - Haz clic en el botón `Run` en la esquina superior derecha o usa `Shift + F10` para ejecutar el programa.

## Ejecutar el Programa desde la Línea de Comandos

Si prefieres ejecutar el programa desde la terminal, asegúrate de estar en el directorio raíz del proyecto y ejecuta:


```bash
cd <path_proyecto>
python <Archivo .py del proyecto que quieras ejecutar>
```
