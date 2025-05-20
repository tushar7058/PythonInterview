'''

8. **Finding the Factorial of a Number**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Mathematical Computations  
   **Description**: Write a program to compute the factorial of a given number.  
   **Example**:  
   Input: `number = 5`  
   Output: `120`  
   Explanation: 5! (factorial) is 5 × 4 × 3 × 2 × 1 = 120.  


'''
# iterative version
def findfactorial(num):
    result = 1
    for i in range(2,num+1):
        result*=i
    return result
print("iterative method",findfactorial(5))

# recursive version
def factorial_recursive(num):
    if num ==0 or num ==1:
        return 1
    return num*factorial_recursive(num-1)
print("recursive method :", factorial_recursive(5))
