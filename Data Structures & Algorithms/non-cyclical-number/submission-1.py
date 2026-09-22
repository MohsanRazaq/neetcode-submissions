class Solution:
    def get_sum(self,n:int)->int:
        curr_sum=0
        while n>0:
            dig=n%10
            curr_sum+=dig**2
            n//=10
        return curr_sum


    def isHappy(self, n: int) -> bool:
        slow=n
        fast=self.get_sum(n)

        while fast!=1 and slow!=fast:
            slow=self.get_sum(slow)
            fast=self.get_sum(self.get_sum(fast))

        return fast==1
    # time complexity O(logn) space complexity O(1)

         
        