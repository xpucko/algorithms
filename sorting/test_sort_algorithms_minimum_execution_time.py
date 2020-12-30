"""
By executing this code you can see the difference in the duration of the algorithms.
Time varies with the power of the computer and the generation of shuffled numbers. I got these result:

Sample test with 5000 shuffled integers, each of them between 0 and 1000.
* radix_sort - minimum execution time of 10 times: 0.0710534669997287
* quick_sort - minimum execution time of 10 times: 0.1423605489981128
* merge_sort - minimum execution time of 10 times: 0.22796103400469292
* shell_sort - minimum execution time of 10 times: 0.24222833699604962
* heap_sort - minimum execution time of 10 times: 0.3830465790015296
* selection_sort - minimum execution time of 10 times: 10.672649225998612
* insertion_sort - minimum execution time of 10 times: 11.74724064500333
* bubble_sort - minimum execution time of 10 times: 26.85097425999993
"""

from random import randint
from timeit import repeat
from radix_sort import radix_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from shell_sort import shell_sort
from heap_sort import heap_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=5, number=10)
    print(f"* {algorithm} - minimum execution time of 10 times: {min(times)}")


if __name__ == "__main__":
    length, start, end = 5000, 0, 1000
    arr = [randint(start, end) for _ in range(length)]
    print(f'Sample test with {length} shuffled integers, each of them between {start} and {end}.')
    run_sorting_algorithm('radix_sort', array=arr)
    run_sorting_algorithm('quick_sort', array=arr)
    run_sorting_algorithm('merge_sort', array=arr)
    run_sorting_algorithm('shell_sort', array=arr)
    run_sorting_algorithm('heap_sort', array=arr)
    run_sorting_algorithm('selection_sort', array=arr)
    run_sorting_algorithm('insertion_sort', array=arr)
    run_sorting_algorithm('bubble_sort', array=arr)
