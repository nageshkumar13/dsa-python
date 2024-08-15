# Reverse a String: Implement a recursive function to reverse a string.

class Solution:
    def reverse_string(self, a):
        # Base case: when the string is empty
        if len(a) == 0:
            return a
        # Recursive case: reverse the rest of the string and add the first character at the end
        return a[-1] + self.reverse_string(a[:-1])

solution = Solution()

name = "alice"

res = solution.reverse_string(name)

print(res)
