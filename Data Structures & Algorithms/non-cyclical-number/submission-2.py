class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            # Inline digit sum for speed
            curr_sum = 0
            while n > 0:
                n, dig = divmod(n, 10)
                curr_sum += dig * dig
            n = curr_sum
            
        return n == 1
      
