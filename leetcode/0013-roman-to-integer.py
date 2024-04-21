class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        combinate = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        number = 0
        ignores_next = False
        for index, char in enumerate(s):
            if ignores_next: 
                ignores_next = False
                continue
            try: v = char + s[index+1]
            except IndexError: v = char
            if v not in combinate:
                number += romans[char]
            else: 
                number += combinate[v]
                ignores_next = True
        return number
    
# This is a solution that needs less lines. By the users of LeetCode:
# m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# ans = 0
# for i in range(len(s)):
#   if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
#       ans -= m[s[i]]
#   else:
#       ans += m[s[i]]
# return ans