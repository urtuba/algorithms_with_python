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
