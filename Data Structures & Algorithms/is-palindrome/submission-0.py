class Solution:
    def alphanum(self,char):
        return (ord('A')<=ord(char)<=ord('Z') or 
                ord('a')<=ord(char)<=ord('z') or 
                ord('0')<=ord(char)<=ord('9'))

    def isPalindrome(self, s: str) -> bool:
        lp,rp=0,len(s)-1
        while lp<rp:
            while lp<rp and not self.alphanum(s[lp]):
                lp+=1
            while rp>lp and not self.alphanum(s[rp]):
                rp-=1

            if s[lp].lower()!=s[rp].lower():
                return False
            lp,rp=lp+1,rp-1
        return True
        
        #Time complexity,O(n), scan linearly
        #space complexity.O(1), without any extra checking characters in place