# Given an array arr[] of non-negative integers and an integer sum, 
# the task is to count all subsets of the given array with a sum equal to a given sum.

# Note: Answer can be very large, so, output answer modulo 10^9+7

def perfectSum(self, arr, n, sum):
    mod=10**9+7
    dp=[[0]*(sum+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(sum+1):
            if arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=(dp[i-1][j]+dp[i-1][j-arr[i-1]])%mod
    return dp[n][sum]