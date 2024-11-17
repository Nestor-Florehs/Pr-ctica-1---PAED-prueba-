import time
from ExtractData import extract_data
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort

dictionary_tasks_parameters_list = extract_data()
print("Data extracted")
aux = [None] * len(dictionary_tasks_parameters_list) # Creamos la array auxiliar

def order_with_merge_sort():

    starting_time = time.time()
    merge_sort(dictionary_tasks_parameters_list, 0, len(dictionary_tasks_parameters_list) - 1, "weight", aux)
    ending_time = time.time()

    elapsed_time_seconds = ending_time - starting_time
    elapsed_time_minutes = elapsed_time_seconds / 60

    # Mostrar lista ordenada.
    """for (i, task_dictionary) in enumerate(dictionary_tasks_parameters_list):
        print(i, f"Task: {task_dictionary["name"]}")
        print(f"\t{task_dictionary["weight"]}")"""

    print("\nSorted with MergeSort")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_seconds, "segundos")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_minutes, "minutos")

def order_with_quick_sort():

    starting_time = time.time()
    quick_sort(dictionary_tasks_parameters_list, 0, len(dictionary_tasks_parameters_list) - 1, "weight")
    ending_time = time.time()

    elapsed_time_seconds = ending_time - starting_time
    elapsed_time_minutes = elapsed_time_seconds / 60

    # Mostrar lista ordenada.
    """for (i, task_dictionary) in enumerate(dictionary_tasks_parameters_list):
        print(i, f"Task: {task_dictionary["name"]}")
        print(f"\t{task_dictionary["weight"]}")"""

    print("Sorted with QuickSort")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_seconds, "segundos")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_minutes, "minutos")

def order_with_insertion_sort():

    starting_time = time.time()
    insertion_sort(dictionary_tasks_parameters_list, "name")
    ending_time = time.time()

    elapsed_time_seconds = ending_time - starting_time
    elapsed_time_minutes = elapsed_time_seconds / 60

    # Mostrar lista ordenada.
    for (i, task_dictionary) in enumerate(dictionary_tasks_parameters_list):
        print(i, f"Task: {task_dictionary["name"]}")

    print("Sorted with InsertionSort")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_seconds, "segundos")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_minutes, "minutos")

order_with_insertion_sort()