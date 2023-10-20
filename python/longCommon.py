#Longest common prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        prefix = strs[0]

        for i in range(len(prefix)):
            if not len(prefix):
                return ""

            else:
                for word in strs:
                    if word[i] != prefix[i]:
                        return prefix[:i]
                    
        
        return prefix

# Working solution