'''


19. **Finding Prime Numbers in a Range**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, Number Theory  
    **Description**: Write a program to find all prime numbers within a given range.  
    **Example**:  
    Input: `range = [10, 30]`  
    Output: `[11, 13, 17, 19, 23, 29]`  
    Explanation: Prime numbers between 10 and 30 are 11, 13, 17, 19, 23, and 29.  


'''
import math
def isPrimeNo(num):
    if num <=1:
        return False
    for i in range(2,int    (math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def findPrimeInRange(start, end):
    prime = []
    for num in range(start,end+1):
        if isPrimeNo(num):
            prime.append(num)
    return prime
start = 30 
end = 100
prime_list = findPrimeInRange(start,end)
print(f" prime numbers between {start} and {end}:",prime_list)