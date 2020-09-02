class Solution:
    def myAtoi(self, str: str) -> int:
        return_str = ""
        start_flag = False
        for c in str:
            if start_flag:
                if c.isdigit(): return_str += c
                else: break
            else:
                if c == ' ': continue
                elif c == '+' or c == '-' or c.isdigit():
                    return_str = c
                    start_flag = True
                else: break
                    
        if len(return_str) == 0 or ((return_str[0] == '+' or return_str[0] == '-') and len(return_str) == 1):
            return 0
        return_int = int(return_str)
        if return_int < -2**31:
            return -2**31
        elif return_int > 2**31 - 1:
            return 2**31 - 1
        else:
            return return_int
