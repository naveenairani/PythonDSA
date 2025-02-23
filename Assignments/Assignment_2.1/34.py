class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        res = []
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                res.append(i)
        return [res[0], res[-1]]