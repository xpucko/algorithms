def radix_sort(array):
    placement = 1
    max_value = max(array)
    while placement <= max_value:
        buckets = [list() for _ in range(10)]

        for value in array:
            index_bucket = int((value / placement) % 10)
            buckets[index_bucket].append(value)

        index = 0
        for index_bucket in range(10):
            for value in buckets[index_bucket]:
                array[index] = value
                index += 1

        placement *= 10
