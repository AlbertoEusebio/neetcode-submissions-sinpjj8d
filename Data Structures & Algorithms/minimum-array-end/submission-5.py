class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        # count up to n-1 into the free bits !!!
        # this is equivalent to setting the free bits to n-1

        # we do this by setting the free bits of X in order with the bits of N-1 (not N because N is set)

        s = n-1 # nuber to set
        # we are going to do so using 2 pointers 
        print(f"Setting {s:0b} into {x:0b}")
        
        for i in range(64):
            if (x & (1 << i)) >> i == 0:
                c = s & 1
                s = s >> 1
                x = x | (c << i)
            
            print(f"{x:0b}")
        return x