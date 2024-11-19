def selection_sort(arr, key='name'):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j][key].lower() < arr[min_idx][key].lower():
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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
    print("Lista ordenada por nombre:")
    for item in arr:
        print(item)

# Ejecutar el test
test_selection_sort()

