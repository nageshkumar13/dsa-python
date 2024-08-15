# Power Calculation: Write a recursive function to calculate x raised to the power n (x^n)

class Solution:
    def calc_power(self, x, n):
        if n == 0:
            return 1
        return x * self.calc_power(x, n-1)
    

solution = Solution()

num = 5
power = 3

res = solution.calc_power(num, power)
print(f"{num} to the power of {power} is {res} .")

