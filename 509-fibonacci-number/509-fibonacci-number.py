class Solution:
    def fib(self, n: int) -> int:
        total = 0
        first = 1
        second = 0
        
        if n<2: return n
        
        for i in range(1, n):
            total = first + second
            second = first
            first = total
        
        return total