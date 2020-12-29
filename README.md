# Sorting algorithms.


## Bubble Sort.
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list. Bubble sort has a worst-case and average complexity of О(n^2), where n is the number of items being sorted. Therefore, bubble sort is not a practical sorting algorithm and is used primarily as an educational tool.

![](https://i.makeagif.com/media/11-24-2015/gI3nus.gif)


### Selection Sort.
The selection sort algorithm sorts an array by repeatedly finding the minimum element  from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array. In every iteration of selection sort, the minimum element from the unsorted subarray is picked and moved to the sorted subarray. Selection sort is not difficult to analyze compared to other sorting algorithms since none of the loops depends on the data in the array. Time Complexity is O(n2) as there are two nested loops.

![](https://gifimage.net/wp-content/uploads/2018/05/selection-sort-gif-12.gif)


## Insertion Sort.
Insertion sort iterates, consuming one input element each repetition, and grows a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain. The algorithm is more efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort.

![](http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/images/InsertionEg02.gif)


## Heap Sort.
Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements. The Heap sort algorithm involves preparing the list by first turning it into a max heap. The algorithm then repeatedly swaps the first value of the list with the last value, decreasing the range of values considered in the heap operation by one, and sifting the new first value into its position in the heap. This repeats until the range of considered values is one value in length. The performance of this algorithm is O(n log n).

![](https://www.codesdope.com/staticroot/images/algorithm/heapsort1.gif)


## Merge Sort.
Merge sort is an efficient, general-purpose, comparison-based sorting algorithm. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted). Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

![](https://gifimage.net/wp-content/uploads/2017/10/merge-sort-gif-5.gif)


## Quick Sort.
Quick sort is an efficient sorting algorithm. It is a divide and conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting. When implemented well, it can be about two or three times faster than its main competitors, merge sort and heap sort.

![](https://assets.digitalocean.com/articles/alligator/js/quick-sort/quick-sort-animation.gif)


## Radix Sort.

## Shell Sort.
