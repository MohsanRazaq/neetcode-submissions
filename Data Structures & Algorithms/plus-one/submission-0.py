class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for num in range(len(digits)-1,-1,-1):

            if digits[num]<9:
                digits[num]+=1
                return digits
            else:
                digits[num]=0

        return [1]+digits

        #Time complexity, O(n), space O(1)