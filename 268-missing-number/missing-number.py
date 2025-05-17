class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target_sum = n*(n+1)/2
        actual_sum = sum(nums)
        return(target_sum-actual_sum)
            