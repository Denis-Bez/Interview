"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example: 
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

nums = [3,2,4]
target = 6

## --- Approach 1 ---
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]   


if __name__ == '__main__':
    ob = Solution1()
    ob.twoSum(nums, target)