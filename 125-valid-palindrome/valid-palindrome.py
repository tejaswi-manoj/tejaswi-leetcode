class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        only_al_num = ""
        for char in s:
            if char.isalnum():
                only_al_num+=char
        print(only_al_num)
        lower_case = only_al_num.lower()
        if lower_case == lower_case[::-1]:
            return True
        else:
            return False