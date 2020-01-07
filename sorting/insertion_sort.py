from random import randint

def insertion_sort(array):
    ## START FROM SECOND ELEMENT, GO TO END ##
    for i in range(1,len(array)):
        ## START CHECK FROM PREVIOUS ELEMENT ##
        j = i - 1
        key = array[i]
        ## SHIFT ARRAY UNTIL FIND CORRECT POSITION FOR KEY ##
        while ((array[j] > key) and (j >= 0)):
            array[j+1] = array[j]
            j = j-1
        ## PLACE KEY TO ITS CORRECT POSITION ##
        array[j+1] = key
    return array

## EXAMPLE ##
def ex_insertion_sort(size):
    array = [randint(1,100) for _ in range (size)]
    print("BEFORE:", array)
    print(" AFTER:", insertion_sort(array))

ex_insertion_sort(15);
