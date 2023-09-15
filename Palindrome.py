# Given a Integer array A[] of n elements. 
# Your task is to complete the function PalinArray. 
# Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

def PalinArray(arr ,n):
    
    for i in arr:
        num = str(i)
        num1 = num[::-1]
        if num1!=num:
            return 0
    return 1