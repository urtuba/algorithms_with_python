# algorithms_with_python

This project is coding for implementing and testing algorithms in python. Functions are written briefly, helper functions are added beside algorithms.

## helper_functions.py

This file contains necessary functions while working on algorithms.

### random_array(size, max)

Creates a array of random elements in the range from 0 to *max* with *size* length. As default, if you do not specify max; function produces numbers from *0* to *size*3*. If you do not specify size also, it is set to 20.

### print_array(array)

It is all for printing a readable version of the array, especially size goes larger it shows its difference.

### test_algorithm(func, size, max)

*size* and *max* are the variables in *random_array* function. *func* argument is the name of function. It creates an array in given size and property, it calls given function then tests its execution time. By doing this, it also provides readable result analysis. 
