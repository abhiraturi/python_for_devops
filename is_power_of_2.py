#Solution 1

'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        self.n = n
        """
        self.n = n
        i=0
        while i < n:
            if (2**i) == n:
                return(True)
            else:
                pass 
            i = i+1
        return(False)

a= int(input("Enter a number "))
x= Solution()
y=x.isPowerOfTwo(a)
if y== True:
    print("True")
else:
    print("False")

'''


# Solution 2:

'''
class Solution(object):
    def isPowerOfTwo(self, n:int) -> bool:
        return False if n<0 else bin(n).count('1')==1
'''
