class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length not equal then obviously it is not angram
        if len(s)!=len(t):
             return False
        count_s={}
        # count frequency of characters
        for char in s:
            count_s[char]=count_s.get(char,0)+1

        for  char in t:
            if char not in  count_s or count_s[char]==0:
                return False
            count_s[char]-=1
        return True

    ## Time complexity O(n), we only traverse string linear
    ##space complexity o(1) ,  dic size capped at  lower case 26 alphabets