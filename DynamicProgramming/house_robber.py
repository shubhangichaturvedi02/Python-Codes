"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_2(nums, current_index, temp_dict):
            #print(current_index, nums[current_index])
            if current_index >= len(nums):
                return 0
            else:
                if current_index not in temp_dict:
                    skipfirsthouse = rob_2(nums, current_index + 1, temp_dict)
                    rob_firsthouse = nums[current_index] + rob_2(nums, current_index+2, temp_dict)

                    temp_dict[current_index] = max(skipfirsthouse, rob_firsthouse)
                return temp_dict[current_index]

        temp_dict = {}
        return rob_2(nums,0,temp_dict)
        