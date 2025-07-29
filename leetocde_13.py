class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res,prev = 0, 0
        dict1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in s[::-1]:
            if dict1[i]>=prev:
                res += dict1[i]
            else:
                res -= dict1[i]
            prev = dict1[i]
        return res
