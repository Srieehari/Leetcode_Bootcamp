class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        

        

        arr = [1]* len(nums)

        pre = 1

        for i in range(len(nums)):

            arr[i] = pre
            pre *= nums[i]

        past = 1

        for i in range(len(nums)-1, -1, -1):

            arr[i]*= past

            past*= nums[i]

        

        return arr






        

        

            

            





            