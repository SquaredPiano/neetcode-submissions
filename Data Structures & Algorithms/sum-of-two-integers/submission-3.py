class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
          1 1 1   
          0 1 0 1
        + 0 0 1 1
        ---------
          1 0 0 0 
        steps:
        1.  take last two bits of a and b
        2.  either we have 0 + 1, 1 + 0, 1 + 1, or 0 + 0
            if it is 1 + 1, we need a carry
            otherwise, we dont
        3.  notice: 1 + 1 = 10 i
            and the sum bit is 1 ^ 1
        """
        MASK = 0xFFFF
        MAX_INT = 0x7FFF
        
        while b:
            carry = ((a&b)<<1)&MASK
            sum_bit = (a^b)&MASK
            a, b = sum_bit, carry
        
        return a if a <= MAX_INT else ~(a^MASK)