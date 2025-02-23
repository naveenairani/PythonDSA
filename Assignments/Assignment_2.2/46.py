class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i,nums):
            if i==len(nums):
                return [[]]
            perms = helper(i+1,nums)
            res = []
            for perm in perms:
                for j in range(len(perm)+1):
                    temp = perm.copy()
                    temp.insert(j,nums[i])
                    res.append(temp)
            return res
        return helper(0,nums)