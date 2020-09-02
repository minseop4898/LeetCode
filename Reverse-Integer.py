class Solution:
    def reverse(self, x: int) -> int:
        reverse_x = int(str(abs(x))[::-1])
        if x < 0: reverse_x *= -1
        if reverse_x <= 2**31-1 and reverse_x >= -2**31:
            return reverse_x
        else:
            return 0
