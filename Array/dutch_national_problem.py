#Array consist of only 0's, 1's and 2's. 
# Write an algorithm to sort  this array 
# in O(n) time complexity and O(1)
#  Space complexity with only one traversal Asked in :

def func_to_sort_0_1_2(array: [int]):
    low = mid = 0
    high = len(array) -1
    pivot = 1

    while mid <= high:
       
        if array[mid] > pivot:
            array[mid], array[high] = array[high], array[mid]
            high-=1

        elif array[mid] < pivot:
            array[mid], array[low] = array[low], array[mid]
            mid+=1
            low+=1
        else:
            mid+=1


a = [1,2,0,1,0,1,2,0,1,0]
func_to_sort_0_1_2(a)

print(a)