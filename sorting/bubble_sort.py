def bubble_sort(array):
    length = len(array)
    for i in range(length):
        is_swapped = False

        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_swapped = True

        if not is_swapped:
            break
