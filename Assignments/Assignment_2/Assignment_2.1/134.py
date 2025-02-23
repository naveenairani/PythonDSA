class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        currentGas = 0
        start = 0
        for i in range(len(gas)):
            currentGas += gas[i] - cost[i]
            if currentGas < 0:
                currentGas = 0
                start = i + 1
        return start