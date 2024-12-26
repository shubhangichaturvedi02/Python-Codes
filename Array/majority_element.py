"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from collections import Counter

class Solution:
    def majorityElement(self, nums: [int]) -> int:

        a = Counter(nums)
        max_occurence = None

        for key, value in a.items():
            if value > (len(nums)//2):
                max_occurence = key 

        return max_occurence 
    
s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))