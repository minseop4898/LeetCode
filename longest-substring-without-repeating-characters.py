class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        max_len = 0
        cur_len = 0
        for i, c in enumerate(s):
            if not c in char_dict:
                cur_len += 1
                char_dict[c] = i
            else:
                max_len = max(max_len, cur_len)
                temp_cur_len = i - char_dict[c]
                for del_c in s[i-cur_len:char_dict[c]+1]:
                    char_dict.pop(del_c)
                cur_len = temp_cur_len
                char_dict[c] = i
        return max(max_len, cur_len)
