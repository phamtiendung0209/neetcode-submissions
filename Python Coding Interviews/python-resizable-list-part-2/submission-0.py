from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)

    return arr1 # .extend() modifies the list in-place and returns None
  

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for elem in arr2:
        if elem not in arr1:
            continue 
        arr1.remove(elem)

    return arr1 

# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))