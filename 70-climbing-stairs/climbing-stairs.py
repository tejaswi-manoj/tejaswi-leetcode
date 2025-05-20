class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 1
        two = 1
        
        for i in range(n-1):

            one = one + two
            two = one - two

        return one


        
        