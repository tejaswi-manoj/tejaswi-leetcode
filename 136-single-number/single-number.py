class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = 1 + hash.get(nums[i], 0)

        for c in hash:
            if hash[c] == 1:
                return c
