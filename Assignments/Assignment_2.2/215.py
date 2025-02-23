import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-elem for elem in nums]
        heapq.heapify(arr)
        for _ in range(k-1):
            heapq.heappop(arr)
        return -heapq.heappop(arr)