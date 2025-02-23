class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in val:
                return [val[x], i]
            val[num] = i
        return []