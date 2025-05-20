'''
11. **Finding the Least Common Multiple (LCM)**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, Number Theory  
    **Description**: Write a program to find the LCM of two numbers.  
    **Example**:  
    Input: `a = 12, b = 15`  
    Output: `60`  
    Explanation: The LCM of 12 and 15 is 60.  


    1. = -> assing
    2. == -> compare 
    3. === -> compare datatype 

    a = 19
    b = 'abc'

    a === b -> false

'''
import math
def LeastcommonFactor(a,b):
    print(math.lcm(a,b))

LeastcommonFactor(12,12)

def leastcommonfactor(a,b):
    for i in range(2,min(a,b)+1):
        if a %i ==0 and b%i ==0:
            return i
    return 1

print('least common factor :',leastcommonfactor(12,12))



            