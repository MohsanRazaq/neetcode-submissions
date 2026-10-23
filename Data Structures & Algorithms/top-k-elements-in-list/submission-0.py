class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}

        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1

        rev_lst=sorted(hashmap.keys(),key=hashmap.get,reverse=True)
        res=[]
        for x in rev_lst:
            if len(res)==k:
                return res
            res.append(x)

        return res
        