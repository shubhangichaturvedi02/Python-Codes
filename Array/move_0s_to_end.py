#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order
#  of the non-zero elements in O(n) Time complexity and O(1) Space complexity with single traversal allowed


def move_0s_to_end(array:[int]):
    n = len(array)
    cnt = 0

    for i in range(n):
        print(i)
        if array[i] != 0:
            array[cnt], array[i] = array[i], array[cnt]
            cnt +=1

a = [0,1,0,3,12]
move_0s_to_end(a)
print(a)

