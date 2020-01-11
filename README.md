# algorithms_with_python

This project is coding for implementing and testing algorithms in python. Functions are written briefly, helper functions are added beside algorithms.

## tester.py

This main file acts as command line program for testing and using algorithms. You can easily test different sorting algorithms without any coding using this file.

## sorting.py

File contains sorting algorithms.

### insertion_sort

1. start from second element of the list
1. compare with other elements backwards
  1. if you found smaller elements after greater elements, position your element after it
  1. if you found all items are smaller than yours, keep it in its current position
1. do this process for every element from second to last

Insertion sort is inefficient algorithm when input size and complexity goes greater.

**best case:** ordered list
**worst case:** reverse ordered list
**time complexity:** O(n<sup>2</sup>)
**space complexity:** O(1)

### reverse_insertion_sort

This is simply reversed *insertion_sort*, I did not implement it separately yet.

### merge_sort

1. divide list by two until obtain 1-sized lists
1. merge two arrays recursively to obtain sorted list
  1. compare first elements of array
  1. take smaller element and continue comparison with next element for that array whose element is used.

**best case = average case = worst case**
**time complexity:** O(n*lg*n)
**space complexity:** O(n)

## helper_functions.py

This file contains necessary functions while working on algorithms.

### random_array(size, max)

Creates a array of random elements in the range from 0 to *max* with *size* length. As default, if you do not specify max; function produces numbers from *0* to *size*3*. If you do not specify size also, it is set to 20.

### print_array(array)

It is all for printing a readable version of the array, especially size goes larger it shows its difference.

### test_algorithm(func, size, max)

*size* and *max* are the variables in *random_array* function. *func* argument is the name of function. It creates an array in given size and property, it calls given function then tests its execution time. By doing this, it also provides readable result analysis.
