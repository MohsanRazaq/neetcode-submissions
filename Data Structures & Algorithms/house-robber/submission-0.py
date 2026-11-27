class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_01,prev_02=0,0
        for mon in nums:
            current=max(prev_01,prev_02+mon)

            prev_02=prev_01
            prev_01=current

        return prev_01
