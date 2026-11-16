class Solution:
    def myPow(self, x: float, N: int) -> float:

        if N < 0:
            x = 1 / x
            N = -N

        result = 1.0
        current_product = x

        while N > 0:
            if N % 2 == 1:
                result *= current_product
            
            current_product *= current_product
            N //= 2

        return result
            