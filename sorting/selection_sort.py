def selection_sort(array):
    length = len(array)

    for i in range(length):
        minimum = i

        for j in range(i + 1, length):
            if array[j] < array[minimum]:
                minimum = j

        if minimum != i:
            array[minimum], array[i] = array[i], array[minimum]
