class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        longest_s = ""
        for i in range(len(s)):
            for j in range(2):
                left_idx, right_idx = i, i + j
                while left_idx >= 0 and right_idx < len(s):
                    if s[left_idx] != s[right_idx]: break
                    else:
                        left_idx -= 1
                        right_idx += 1
                if right_idx - left_idx > 1 and len(longest_s) < right_idx - left_idx - 1:
                    longest_s = s[left_idx+1:right_idx]
        if len(longest_s) == 0:
            return s[0]
        else:
            return longest_s
