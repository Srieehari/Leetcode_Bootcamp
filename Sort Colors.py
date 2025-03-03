class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first = 0
        middle  = 0
        outer = len(nums)-1


        while middle <= outer:

            if nums[middle] == 0 :

                nums[middle], nums[first] = nums[first], nums[middle]
                first += 1
                middle +=1
            elif nums[middle] == 1:
                middle +=1 
            else:
                nums[outer], nums[middle] = nums[middle], nums[outer]
                outer -=1
               

        return nums

            

