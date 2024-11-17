def selection_sort(arr, key='name'):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if isinstance(arr[j], dict) and isinstance(arr[min_index], dict):
                if arr[j][key].lower() < arr[min_index][key].lower():
                    min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Función de prueba para ordenar una lista de diccionarios por el nombre
def test_selection_sort():
    arr = [
        {'name': 'Carlos', 'weight': 70},
        {'name': 'Ana', 'weight': 55},
        {'name': 'Elena', 'weight': 60},
        {'name': 'Pedro', 'weight': 80}
    ]
    print("Lista original:", arr)
    selection_sort(arr)
    print("Lista ordenada por nombre:", arr)

# Ejecutar el test
# test_selection_sort()

