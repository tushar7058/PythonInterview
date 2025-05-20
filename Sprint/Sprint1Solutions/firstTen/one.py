'''

1. **Determining Even/Odd Numbers**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming  
   **Description**: Write a program to check whether a number is even or odd.  
   **Example**:  
   Input: `number = 4`  
   Output: `Even`  
   Explanation: Since 4 is divisible by 2, it is an even number. 

'''

n = int(input("Enter a number to check :"))
def evenOdd(n):
    if n%2 ==0:
        print("No is even")
    else :
        print("No is oddd")
evenOdd(n)