class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False

        for char in s:
            if char in t:
                if t.count(char)!=s.count(char):
                    return False
                continue
            return False
        return True