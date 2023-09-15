# Given a number N, check if a number is perfect or not. 
# A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number. 
# Return 1 if the number is Perfect otherwise return 0.

class Solution:
    def isPerfectNumber(self, N):
        if N <= 1:
            return 0 
        sum_of_factors = 1
        for i in range(2, int(N**0.5) + 1):
            if N % i == 0:
                sum_of_factors += i
                if i != N // i:
                    sum_of_factors += N // i
        if sum_of_factors == N:
            return 1
        else:
            return 0