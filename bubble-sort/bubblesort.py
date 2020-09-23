def bubblesort(arr):
  for i in range(len(arr)-2, 0, -1):
    swapped = False
    for j in range(i+1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
        swapped = True
    if not swapped:
      break

arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
bubblesort(arr)
print arr