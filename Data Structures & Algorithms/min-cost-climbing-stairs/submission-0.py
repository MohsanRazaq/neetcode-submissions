class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        first = 0
        second = 0
        
        for i in range(2, len(cost) + 1):
            current = min(second + cost[i - 1], first + cost[i - 2])
            
            first = second
            second = current
            
        return second