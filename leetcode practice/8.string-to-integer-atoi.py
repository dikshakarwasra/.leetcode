#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        result = 0

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1

        return result
        
        
        
# @lc code=end

