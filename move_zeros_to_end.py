class Solution(object):
    def moveZeroes(self, num):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.num=num
        num.sort()
        n=num.count(0)
        return(num[n:] + num[:n])

a=Solution()
zeros_at_end_list=a.moveZeroes([0,1,0,3,12])
print(zeros_at_end_list)