def mergesort(arr):
  print arr
  if len(arr) > 1:
    half = len(arr) // 2
    a = mergesort(arr[:half])
    b = mergesort(arr[half:])
    return merge(a, b)
  else:
    return arr

def merge(a, b):
  print a, b
  i, j = 0, 0
  ret = []
  while i < len(a) or j < len(b):
    if i < len(a) and j < len(b):
      if a[i] < b[j]:
        ret.append(a[i])
        i += 1
      else:
        ret.append(b[j])
        j += 1
    elif i < len(a):
      ret.append(a[i])
      i += 1
    else:
      ret.append(b[j])
      j += 1
  print ret
  return ret

arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
result = mergesort(arr)
print result