class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count each element
        count = Counter(nums) 

        for n, c in count.items():
            if c==1:
                return n
