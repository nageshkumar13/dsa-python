# Sum of Digits: Create a recursive function to find the sum of the digits of a given number.

class Solution:
    def sum_digits(self, n):
        if n < 10:
            return n  
        return n % 10 + self.sum_digits(n // 10)

# Usage example:
num = 12345
solution = Solution()
print(solution.sum_digits(num))
