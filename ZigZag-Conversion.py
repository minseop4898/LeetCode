class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 3 or numRows == 1:
            return s
        elif numRows == 2:
            return s[::2] + s[1::2]
        
        return_s = self.start_end(s, 0, 4+2*(numRows-3))
        for row in range(1,numRows-1):
            even_flag = False
            idx = row
            while idx < len(s):
                return_s += s[idx]
                if even_flag:
                    idx += 2*row
                    even_flag = False
                else:
                    idx += 2*(numRows-row-1)
                    even_flag = True
        return return_s + self.start_end(s, numRows-1, 4+2*(numRows-3))
            
    
    def start_end(self, s: str, start_idx: int, add_num: int) -> str:
        return_s = ""
        while start_idx < len(s):
            return_s += s[start_idx]
            start_idx += add_num
            print('a')
        return return_s
