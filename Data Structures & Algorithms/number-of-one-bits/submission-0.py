class Solution:
    def hammingWeight(self, n: int) -> int:
        total_ones=0

        while n>0:
            if n%2==1:
                total_ones+=1
            n=n//2
        return total_ones

        # time complexity, O(1),space complexity O(1)
        