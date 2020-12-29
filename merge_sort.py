def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]

        merge_sort(left)
        merge_sort(right)

        idx_left = idx_right = idx_arr = 0
        length_left, length_right = len(left), len(right)
        while idx_left < length_left and idx_right < length_right:
            if left[idx_left] < right[idx_right]:
                array[idx_arr] = left[idx_left]
                idx_left += 1
            else:
                array[idx_arr] = right[idx_right]
                idx_right += 1
            idx_arr += 1

        while idx_left < length_left:
            array[idx_arr] = left[idx_left]
            idx_left += 1
            idx_arr += 1

        while idx_right < length_right:
            array[idx_arr] = right[idx_right]
            idx_right += 1
            idx_arr += 1
