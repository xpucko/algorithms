def shell_sort(array):
    length = len(array)
    gap = len(array) // 2

    while gap > 0:

        for i in range(gap, length):
            value = array[i]
            j = i

            while j >= gap and array[j - gap] > value:
                array[j] = array[j - gap]
                j -= gap

            array[j] = value

        gap //= 2
