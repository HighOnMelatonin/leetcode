# Search in a rotated sorted array

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
            
        else:
            return -1

# Working solution, not the most creative but hey