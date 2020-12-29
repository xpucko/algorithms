def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array.pop()
    lower, greater = [], []
    [(lower if x < pivot else greater).append(x) for x in array]

    return quick_sort(lower) + [pivot] + quick_sort(greater)
