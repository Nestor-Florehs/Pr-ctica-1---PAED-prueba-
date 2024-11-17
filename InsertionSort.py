def is_sorted(arr, clave):
    """Verifica si la lista ya está ordenada según la clave."""
    return all(arr[i][clave].lower() <= arr[i + 1][clave].lower() for i in range(len(arr) - 1))

def binary_search(arr, key_item, clave, low, high):
    """Encuentra la posición de inserción usando búsqueda binaria."""
    key_value_lower = key_item[clave].lower()
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][clave].lower() > key_value_lower:
            high = mid - 1
        else:
            low = mid + 1
    return low

def insertion_sort(arr, clave):
    """Insertion Sort optimizado con detección previa de orden."""
    if is_sorted(arr, clave):
        return

    for i in range(1, len(arr)):
        key_item = arr[i]

        # Encuentra la posición con búsqueda binaria
        pos = binary_search(arr, key_item, clave, 0, i - 1)

        # Mueve los elementos en bloque para hacer espacio
        arr[pos + 1 : i + 1] = arr[pos:i]

        # Inserta el elemento en la posición correcta
        arr[pos] = key_item

# Prueba del algoritmo
def test_insertion_sort():
    tasks = [
        {"name": "AAABBB", "weight": 5},
        {"name": "AAAABB", "weight": 12},
        {"name": "ZZZSS", "weight": 32},
        {"name": "Task B", "weight": 2},
        {"name": "C", "weight": 3},
        {"name": "ZZZZZ", "weight": 1},
        {"name": "Task D", "weight": 35},
        {"name": "Task E", "weight": 155},
        {"name": "Task F", "weight": 43},
        {"name": "ZZZZZ", "weight": 23},
    ]

    print("Lista original:")
    for task in tasks:
        print(task)

    # Aplicar Insertion Sort
    insertion_sort(tasks, "name")

    print("\nLista ordenada:")
    for task in tasks:
        print(task)

# test_insertion_sort()
