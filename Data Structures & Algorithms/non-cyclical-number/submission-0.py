class Solution:
    def isHappy(self, n: int) -> bool:
        already_seen=set()

        while n!=1:
            curr_sum=0
            while n>0:
                dig=n%10
                curr_sum+=dig**2
                n//=10
            n=curr_sum

            if n in already_seen:
                return False

            already_seen.add(n)

        return True
        # time complexity O(log n) space  complexity,O(log n