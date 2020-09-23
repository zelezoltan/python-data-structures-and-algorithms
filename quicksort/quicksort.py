"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    return quicksort_(array, 0, len(array) - 1)
    
def quicksort_(array, low, high):
    if high - low <= 0:
        return array
    
    pivot = high
    print array[low:high+1]
    i = low
    while i < pivot:
        if array[i] > array[pivot]:
            array[pivot], array[pivot - 1] = array[pivot - 1], array[pivot]
            if i < pivot - 1:
                array[pivot], array[i] = array[i], array[pivot]
            pivot -= 1
        else:
            i += 1
    quicksort_(array, low, pivot - 1)
    quicksort_(array, pivot + 1, high)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)