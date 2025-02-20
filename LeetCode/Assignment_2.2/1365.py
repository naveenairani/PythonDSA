class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        res = []
        for i, inum in enumerate(nums):
            for j, jnum in enumerate(nums):
                if inum > jnum and i != j:
                    count += 1
            res.append(count)
            count = 0
        return res