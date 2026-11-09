class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        res=right
        import math
        while left<=right:
            mp=(left+right)//2

            total_hours=sum(math.ceil(pile/mp)for pile in piles)
            if total_hours<=h:
                res=mp
                right=mp-1
            else:
                left=mp+1
        return res

#time complexity  O(nlogm