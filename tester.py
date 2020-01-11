### TEST ALGORITHMS
import helper_functions

while True:
    print("TEST SORTING ALGORITHMS: LIST OF FUNCTIONS FOR THEM")
    print("1. insertion_sort")
    print("2. reverse_insertion_sort")
    print("3. merge_sort")
    print("4. quick_sort")
    print("5. counting_sort")
    print("SELECT FUNCTION( USING FUNC NAME ):")
    func = str(input(">>> "))
    print("SELECT ARRAY SIZE:")
    size = int(input(">>> "))
    print("SELECT MAX NUMBER")
    max  = int(input(">>> "))
    helper_functions.test_algorithm(func, size, max)
    print("\nCONTINUE (Y/N):")
    if input(">>> ")=='N':
        break
    else:
        print('')
