class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        arr = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            comp = -nums[i]
            j, k = i+1, n-1
            while j<k:
                if nums[j] + nums[k] == comp:
                    arr.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > comp:
                    k -= 1
                else:
                    j += 1
        return arr