class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        Sum = 0
        while(left<=right):
            Sum += self.nums[left]
            left += 1
        return Sum