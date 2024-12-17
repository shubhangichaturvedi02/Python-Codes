#You have an array of non-negative integers,you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index in O(n) Time complexity and O(1)

#example:
"""
Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 -> 9)
Explanation: Jump from 1st element to 2nd element as there is only 1 step, now there are three options 5, 8 or 9. If 8 or 9 is chosen then the end node 9 can be reached. So 3 jumps are made.



Input : arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
Output: 10

Explanation: In every step a jump is needed so the count of jumps is 10.
"""
def min_jump(arr:[int]):
    n = len(arr)
    if n <= 1:  # no. of jumps needed to reach start index is 0
        return 0
    
    if arr[0] >= n-1: # first index value gurantees only one jump is needed
        return 1
    
    if arr[0] == 0:
        return -1
    
    maxreach = arr[0]
    steps = arr[0]
    jump = 1

    for i in range(1,n):
        if i == n-1:
            return jump
        if arr[i] >= n-1 -i:
            return jump+1

        maxreach = max(maxreach, arr[i] + i)

        steps-=1

        if steps== 0:
            jump+=1

        if i >= maxreach:
            return -1
        
        steps = maxreach - i

    return -1




a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

print("Minimum no. of jumps required is ", min_jump(a))
