# Two Sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                j = nums.index(target - nums[i])
                if j == i:
                    continue
                else:
                    return [i,j]

# Working solution