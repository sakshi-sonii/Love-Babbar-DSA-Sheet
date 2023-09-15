# Given an array Arr of N positive integers. 
# Your task is to find the elements whose value is equal to that of its index value 
# ( Consider 1-based indexing )

#User function Template for python3

class Solution:
      def valueEqualToIndex(self, arr , n ):
            count=[]
            for i in range(1,n+1):
                if i==arr[i-1]:
                    count.append(i)
            return count