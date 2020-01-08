"""
GITHUB: URTUBA
AUTHOR: SAMED KAHYAOGLU
..DATE: 08.01.2019
"""

def random_array(size = 20, max = 0):
    """
    CREATE TEST INPUT AS ARRAY(LIST)
    ARG size: LENGTH OF ARRAY
    ARG max: MAXIMUM VALUE FOR ELEMENTS
    """
    if max == 0:
        max = size * 3
    from random import randint
    return [randint(0, max) for _ in range(size)]

def print_array(array):
    """
    PRINTS OUT GIVEN ARRAY IN ORDER
    """
    size = len(array)
    print('[', end='')
    for i in range(size):
        ## for same indentification
        if (i%10 == 0) and (i != 0):
            print(' ', end="")
        ## printing out with same width
        print(f"{array[i]:5d}", end=' ')
        if size - 1 != i: print(',', end='')
        if i%10 == 9:
            print('')
    print(']')

def test_algorithm(func, size=20, max=0):
    """
    RUNS GIVEN FUNCTIONS AND OUTPUTS ANALYSIS
    ARG func = NAME OF ALGORITHM FUNCTION
    ARG size = SIZE OF INPUT
    ARG max = MAX INPUT VALUE
    """
    import timeit
    ## ARRAY CREATION
    a = create_array(size, max)
    print("INPUT ARRAY:")
    print_array(a)
    print("\n")

    ## EXECUTION
    start = timeit.default_timer()
    test = """
a = {}(a)
print('OUTPUT ARRAY:')
print_array(a)
    """.format(func)
    exec(test)
    stop = timeit.default_timer()

    ## OUTPUT AND ANALYSIS
    print(
        f"\nALGORITHM ANALYSIS RESULTS",
        f"\n{'ALGORITHM:':>15}{func:>20}",
        f"\n{'INPUT SIZE:':>15}{len(a):>10} Integers",
        f"\n{'EXECUTION TIME:':>15}{int((stop-start)*1000000):>10} Microseconds"
    )
