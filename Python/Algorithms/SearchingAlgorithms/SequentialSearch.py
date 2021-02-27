# Implementation of Sequential Search in Python
#If element is found then return its Position
#If Not found then return -1

def sequential_search(arr, ele):

  pos = 0
  l = len(arr)
  found = False

  while pos != l and not found:

    if ele == arr[pos]:
      found = True

    pos += 1

  if found:
    return pos-1

  else:
    return -1


# Driver Code
array = [int(x) for x in input("Enter elements separated by space: ").split(" ")]
element = int(input("Enter element to search: "))
result = sequential_search(array, element)

if result >= 0:
  print("Found at Postion {}".format(result))

else:
  print("Not Found")