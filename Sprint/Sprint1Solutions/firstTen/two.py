'''

2. **Checking for Prime Numbers**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Number Theory  
   **Description**: Write a program to determine if a number is prime.  
   **Example**:  
   Input: `number = 7`  
   Output: `Prime`  
   Explanation: 7 has no divisors other than 1 and itself, so it is a prime number. 


   - prime-> 1 , 3, 5,7, 11, 13,etc
   - divide by only that number
   -  

'''
num = int(input("Enter a num :"))
def checkprimeNo(num):
    if num <=1:
        print("Num is not prime")
        return  
  #  for i in range(2,10): # for perticular range.
    for i in range(2, int(num ** 0.5) + 1):   # for all sqrt range . 
        if num %i ==0:
            print("Num is not prime ")
            break
    else:
        print("no is prime num")

checkprimeNo(num)