# Given two numbers X and Y, and a range [L, R] where 1 <= L <= R <= 32. 
# You have to copy the set bits of 'Y' in the range L to R in 'X'. 
# Return this modified X.

# Note: Range count will be from Right to Left & start from 1.

class Solution:
    def setSetBit(self, x, y, l, r):
        pos = 1
        a = []
        while(pos<=r):
            if y%2!=0 and pos>=l:
                a.append(pos)
            pos = pos+1
            y = y>>1
        num = 0 
        for i in a:
            num = num+(1<<i-1)
        ans = num|x
        return(ans)