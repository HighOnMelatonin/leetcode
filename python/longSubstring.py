# Longest substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = 0
        front = 0
        rear = 0
        for c in s:
            while c in s[front:rear]:
                front += 1

            rear += 1
            if (rear - front) > num:
                num = rear - front

        return num

# Working solution