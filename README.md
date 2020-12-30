# Sorting algorithms.


## Bubble Sort
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list. Bubble sort has a worst-case and average complexity of О(n^2), where n is the number of items being sorted. Therefore, bubble sort is not a practical sorting algorithm and is used primarily as an educational tool.

![](https://i.makeagif.com/media/11-24-2015/gI3nus.gif)


## Selection Sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element  from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array. In every iteration of selection sort, the minimum element from the unsorted subarray is picked and moved to the sorted subarray. Selection sort is not difficult to analyze compared to other sorting algorithms since none of the loops depends on the data in the array. Time Complexity is O(n2) as there are two nested loops.

![](https://stackabuse.s3.amazonaws.com/media/selection-sort-in-javascript-1.gif)


## Insertion Sort
Insertion sort iterates, consuming one input element each repetition, and grows a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain. The algorithm is more efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort.

![](http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/images/InsertionEg02.gif)


## Heap Sort
Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements. The Heap sort algorithm involves preparing the list by first turning it into a max heap. The algorithm then repeatedly swaps the first value of the list with the last value, decreasing the range of values considered in the heap operation by one, and sifting the new first value into its position in the heap. This repeats until the range of considered values is one value in length. The performance of this algorithm is O(n log n).

![](http://www-scf.usc.edu/~zhan468/public/Notes/resources/7073C729230E1A2C3C3C9207B25F6B43.gif)


## Merge Sort
Merge sort is an efficient, general-purpose, comparison-based sorting algorithm. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted). Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

![](https://gifimage.net/wp-content/uploads/2017/10/merge-sort-gif-5.gif)


## Quick Sort
Quick sort is an efficient sorting algorithm. It is a divide and conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting. When implemented well, it can be about two or three times faster than its main competitors, merge sort and heap sort.

![](http://www-scf.usc.edu/~zhan468/public/Notes/resources/C411339B79F92499DCB7B5F304C826F4.gif)


## Radix Sort
Radix sort is a non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets according to their radix. For elements with more than one significant digit, this bucketing process is repeated for each digit, while preserving the ordering of the prior step, until all digits have been considered. For this reason, radix sort has also been called bucket sort and digital sort. The time complexity of radix sort is O(d*(n+b)), where d is the number of digits in the given list, n is the number of elements in the list, and b is the base or bucket size used, which is normally base 10 for decimal representation.

![](https://images3.programmersought.com/732/11/1116fc068eb921646b37275cc5bf65bc.gif)


## Shell Sort
Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm. This algorithm avoids large shifts as in case of insertion sort, if the smaller value is to the far right and has to be moved to the far left. This algorithm uses insertion sort on a widely spread elements, first to sort them and then sorts the less widely spaced elements.

![](https://i.makeagif.com/media/8-25-2016/mKGEkd.gif)


# The complexity
Analysis of an algorithm's complexity is helpful when comparing algorithms or seeking improvements. By studying time complexity we will understand the important concept of efficiency and will be able to find bottlenecks in our code which should be improved, mainly when working with huge data sets.
Every sorting algorithms has its own advantages and disadvantages, their complexity can be seen as a way of expressing their own advantages and disadvantages easily according to a specific set of input data. The complexity for sorting algorithms is probably even more important than for data structures. The complexity is expressed on 2 axes, the space and the time. It's usually in terms of time. The space complexity represents the memory consumption of a sorting algorithm.

![](http://blog.benoitvallon.com/img/2016-03-12-sorting-algorithms-in-javascript/big-o.png)

The Big-O notation is the standard metric used to measure the complexity of an algorithm.

![](http://blog.benoitvallon.com/img/2016-03-12-sorting-algorithms-in-javascript/big-o-complexity.png)
