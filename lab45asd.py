def comb_sort(arr):
    """Сортировка методом прочесывания (Comb Sort)"""
    # Создаем копию, чтобы не изменять исходный массив
    arr_copy = arr.copy()
    n = len(arr_copy)
    gap = n
    shrink = 1.3
    sorted_status = False

    while not sorted_status:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_status = True

        for i in range(0, n - gap):
            if arr_copy[i] > arr_copy[i + gap]:
                arr_copy[i], arr_copy[i + gap] = arr_copy[i + gap], arr_copy[i]
                sorted_status = False
                
    return arr_copy


def insertion_sort(arr):
    """Сортировка вставками (Insertion Sort)"""
    # Создаем копию, чтобы не изменять исходный массив
    arr_copy = arr.copy()
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
            
        arr_copy[j + 1] = key
        
    return arr_copy


# Пример использования и проверка работы
if __name__ == "__main__":
    # Исходная последовательность чисел
    numbers = [34, -2, 10, -9, 0, 75, 4, 11, 23, -50]
    
    print("=== ИСХОДНЫЕ ДАННЫЕ ===")
    print(f"Последовательность: {numbers}\n")
    
    print("=== РЕЗУЛЬТАТЫ СОРТИРОВОК ===")
    
    # Вызов сортировки методом прочесывания
    result_comb = comb_sort(numbers)
    print(f"№4 Метод прочесывания: {result_comb}")
    
    # Вызов сортировки вставками
    result_insertion = insertion_sort(numbers)
    print(f"№5 Вставками:          {result_insertion}")
