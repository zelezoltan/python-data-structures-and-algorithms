"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    ind_first, ind_last = 0, len(input_array) - 1
    half = (ind_last + ind_first) // 2
    while(input_array[half] <> value and ind_first < ind_last):
        if input_array[half] < value:
            ind_first = half + 1
        else:
            ind_last = half - 1
        half = (ind_last + ind_first) // 2
    if input_array[half] == value:
        return half
    else:
        return -1

def bin_search(arr, value):
  low, high = 0, len(arr) - 1
  while(low <= high):
    mid = (low + high) // 2
    if arr[mid] == value:
      return mid
    elif arr[mid] < value:
      low = mid + 1
    else
      high = mid - 1 
  return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)