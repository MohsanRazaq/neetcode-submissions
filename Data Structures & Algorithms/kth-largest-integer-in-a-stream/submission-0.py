class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.top_k = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        self.top_k.append(val)
        self.top_k.sort(reverse=True)
        
        if len(self.top_k) > self.k:
            self.top_k.pop() 
            
        return self.top_k[-1]