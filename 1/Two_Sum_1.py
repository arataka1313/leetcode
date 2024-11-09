from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
solution = Solution()

nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)