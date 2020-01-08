def insertion_sort(array):
    """
    INSERTION SORT ALGORITHM
    ARG array = LIST(ARRAY) OF NUMBERS
    """
    size = len(array)
    for j in range(1, size):
        key = array[j]  ## copies the element for comparison
        i = j - 1       ## starts comparing with lower order numbers
        while (i >= 0) and (array[i] > key):
            ## When the number is bigger than key, key moves left
            array[i+1] = array[i]
            i = i-1
        ## Key is copied to its sorted place
        array[i+1] = key
    return array

def reverse_insertion_sort(array):
    """
    REVERSE INSERTION SORT USES INSERTION SORT FUNCTION
    """
    array =  insertion_sort(array)
    return array[::-1]
