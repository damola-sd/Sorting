# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    if arrA is None:
        # if they are assign an empty array to them
        arrA = []
    if arrB is None:
        arrB = []

    # while length of arrA or length of arrB is bigger than zero
    while len(arrA) > 0 or len(arrB) > 0:
        # if length of arrA is 0
        if len(arrA) == 0:
            # append the first item from arrB into merged array
            merged_arr.append(arrB.pop(0))

        # if length of arrB is 0
        elif len(arrB) == 0:
            # append the first item from arrA into merged array
            merged_arr.append(arrA.pop(0))

        # if the first item of arrA is smaller than the first item of arrB
        elif arrA[0] < arrB[0]:
            # append the first item of arrA into merged array
            merged_arr.append(arrA.pop(0))

        # if the first item of arrayB is smaller than the first item of arrayA
        elif arrB[0] < arrA[0]:
            # append the first item of arrB into merged array
            merged_arr.append(arrB.pop(0))

    # return merged_arr
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len( arr ) > 1:
        middle = len(arr)/2
        left = merge_sort( arr[ 0 : middle ] )
        right = merge_sort( arr[ middle : ] )
        arr = merge( left, right )
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
