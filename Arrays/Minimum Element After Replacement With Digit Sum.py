#3300. Minimum Element After Replacement With Digit Sum
class Solution:
    def minElement(self, nums):
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        return min(digit_sum(num) for num in nums)
