class Solution:
    def hammingWeight(self, n: int) -> int:
        counts=0

        while n:
            n=n &(n-1)
            counts+=1

        return  counts  
# time complexity, O(k), space O(1)        