class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for i in range(len(nums)+1):
            arr.append(i)
        # gives us an array of all the integers from 0 to n e.g. arr = [0,1,2,3]
        
        for j, val in enumerate(arr):
            if val not in nums:
                return(val)
            
            