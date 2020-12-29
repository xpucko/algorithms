def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1

        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = value


def insertion_sort_2(array):
    for i in range(1, len(array)):
        value = array[i]

        while i > 0 and array[i - 1] > value:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
