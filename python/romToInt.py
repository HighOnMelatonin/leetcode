# Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        if len(s) <= 2:
            if len(s) < 2:
                num = symbols[s[0]]

            elif symbols[s[0]] >= symbols[s[1]]:
                num = symbols[s[0]] + symbols[s[1]]

            else:
                num = symbols[s[1]] - symbols[s[0]]
        
        else:
            for i in range(len(s) - 2, -1, -1):
                if symbols[s[i]] >= symbols[s[i + 1]]:
                    num += symbols[s[i]]

                else:
                    num -= symbols[s[i]]

            num += symbols[s[-1]]    

        return num

# Working solution