class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        for i in range(len(nums)):
            if i in nums:
                pass
            else:
                return(i)

a=Solution()
list_1=[]
element=input("Enter a elements for the list ")
while True:
    element=input("Enter a elements for the list ")
    if element=="":
        break
    else:
        list_1.append(element)


missing_number=a.missingNumber(list_1)
print(missing_number)