#Fibonacci Sequence: Implement a recursive function to generate the nth Fibonacci number.

class Solution:    
    def fibo(self, n):
        #base condition
        if n <= 1:
            return n       
        return self.fibo(n-1) + self.fibo(n-2)

num = 4
solution = Solution()
res = solution.fibo(num)



print(f"No. {num} fibonacci-number is {res} .")

