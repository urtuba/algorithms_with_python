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

def merge_sort(array):
    """
    SORTS ARRAY BY USING INSERTION SORT ALGORITHM
    ARG array = LIST(ARRAY) OF NUMBERS
    """
    if len(array) <= 1:
        return array
    else:
        left  = merge_sort(array[int( len(array)/2 ):])
        right = merge_sort(array[:int( len(array)/2 )])

        return merge(left,right)

def merge(left, right):
    """
    SUBFUNCTION OF MERGE SORT, COMBINES 2 SORTED ARRAYS AS ONE SORTED ARRAY
    ARG left = FIRST ARRAY
    ARG right = SECOND ARRAY
    """
    merged = []
    leftIdx, rightIdx = 0, 0

    while (leftIdx < len(left)) and (rightIdx < len(right)):
        if left[leftIdx] < right[rightIdx]:
            merged.append(left[leftIdx])
            leftIdx += 1
        else:
            merged.append(right[rightIdx])
            rightIdx += 1

    ## one of two arrays are done, rest of other are added to returning array
    if leftIdx == len(left):
        merged.extend(right[rightIdx:])
    else:
        merged.extend(left[leftIdx:])
    return merged

def quick_sort(array):
    """
    SORTING FUNC USING QUICK SORT ALGORITHM
    ARG array = LIST(ARRAY) of NUMBERS
    """
    if len(array) <= 1:
        return array

    from random import randint
    smaller, equal, larger = [], [], []
    pivot = array[randint(0, len(array)-1)]

    for n in array:
        if n < pivot:       smaller.append(n)
        elif n == pivot:    equal.append(n)
        else:               larger.append(n)

    return quick_sort(smaller) + equal + quick_sort(larger)

def counting_sort(array):
    """
    SORTING FUNCTION USING COUNTING SORT ALGORITHM
    ARG array = LIST(ARRAY) OF NUMBERS
    """
    ## counter lists has elements for every
    maximum = max(array)
    counter = [0]*(maximum+1)

    for i in range(len(array)):
        counter[array[i]] += 1

    for i in range(1, maximum + 1):
        counter[i] = counter[i] + counter[i-1]

    #print_array(counter)

    result = [0]*len(array)
    for i in range(len(array)):
        result[counter[array[i]] -1] = array[i]
        counter[array[i]] -= 1

    return result

def count_sort(array, exp):
    """
    SUBFUNCTION OF RADIX SORT
    ARG array = LIST OF NUMBERS
    ARG exp = WHICH EXPOTENTIAL WILL BE USED FOR COUNTING
    """
    ## array of remeinders
    expArray = list(array)
    for i in range(len(array)):
        expArray[i] = array[i] % (10**exp)
    maximum = max(expArray)
    counter = [0] * (maximum+1)

    ## standard counting sort process
    for i in range(len(expArray)):
        counter[expArray[i]] += 1
    for i in range(1, maximum+1):
        counter[i] = counter[i] + counter[i-1]

    result = [0]*len(expArray)
    for i in range(len(array)):
        result[counter[expArray[i]] - 1] = array[i]
        counter[expArray[i]] -= 1
    return result


def radix_sort(array):
    from math import log10, ceil
    maximum = max(array)
    max_exp = ceil(log10(maximum))
    ## calling for each exp
    for i in range(1,max_exp+1):
        array = count_sort(array, i)
    return array
