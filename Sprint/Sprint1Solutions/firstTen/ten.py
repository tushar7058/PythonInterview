'''

10. **Finding the Greatest Common Divisor (GCD)**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, Number Theory  
    **Description**: Write a program to find the GCD of two numbers.  
    **Example**:  
    Input: `a = 48, b = 18`  
    Output: `6`  
    Explanation: The GCD of 48 and 18 is 6.

'''


def findGCD(n):
    pass


def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

print(gcd_recursive(48, 18))  # Output: 6



import math

print(math.gcd(48, 18))  # Output: 6



def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
print(gcd(48, 18))  # Output: 6