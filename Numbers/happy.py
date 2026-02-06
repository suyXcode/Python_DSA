class Solution:
    def isHappy(self,n):
        while n>9:
            sum = 0
            while n>0:
                sum += (n%10)**2
                n //= 10
            n = sum
        return n == 1 or n == 7
    
# Example Usage :
sol = Solution()
n = int(input("Enter a number: "))
print(f"Is {n} a happy number = {sol.isHappy(n)}")  # Output: True