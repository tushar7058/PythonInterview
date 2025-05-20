'''
9. **Summing Digits of a Number**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Mathematical Computations  
   **Description**: Write a program to calculate the sum of digits of a number.  
   **Example**:  
   Input: `number = 1234`  
   Output: `10`  
   Explanation: The sum of the digits 1 + 2 + 3 + 4 = 10.  

'''
n = int(input('enter a number :'))
def sumofNum(n):
    total = 0
    str_num = str(n)
    for i in str_num:
        total +=int(i)
    print("sum is :",total)

sumofNum(n)