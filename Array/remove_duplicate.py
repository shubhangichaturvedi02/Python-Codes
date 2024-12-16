"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
 Do not allocate extra space for another array, Time complexity O(n) and Space complexity O(1)
"""


def remove_duplicate(arr:[int]):
    n = len(arr)

    if n == 0 or n == 1:
        return arr
    j:int = 0

    for i in range(n-1):
        if arr[i]!=arr[i+1]:
            arr[j] = arr[i]
            j+=1

    arr[j] = arr[n-1]

    return j

a = [1,2,2,3,4,4,4,5,5,6]
idx = remove_duplicate(a)
print(a[:idx+1])

