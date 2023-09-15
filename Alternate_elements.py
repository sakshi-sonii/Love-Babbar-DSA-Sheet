# You are given an array A of size N. 
# You need to print elements of A in alternate order (starting from index 0).

def printAl(arr,n):
    # your code here
    for i in range(0,len(arr),2):
        print(arr[i],end = " ")