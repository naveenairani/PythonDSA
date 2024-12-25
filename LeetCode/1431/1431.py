from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= maxcandies)
        return result