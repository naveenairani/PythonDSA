class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rl = range(len(nums)+ 1)
        add = sum(nums) 
        return sum(rl)-add