class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        
        for idx,value in enumerate(nums):
            differ=target-value
            if differ in hash_map:
                return [hash_map[differ],idx]
            hash_map[value]=idx
        return

        #Time complexity O(n), since we only once iterate
        # Space complexity O(n)