'''
4. **Calculating Armstrong Numbers**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Number Theory  
   **Description**: Write a program to check if a number is an Armstrong number.  
   **Example**:  
   Input: `number = 153`  
   Output: `Armstrong Number`  
   Explanation: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.  

'''
num= 154
        
def checkarmstrongnum1(num):
    str_num = str(num)
    power = len(str_num)
    total = 0
    
    for i in str_num:
        total = total+int(i)**power
    if total ==num:
        print("yes")
    else:
        print("not")

checkarmstrongnum1(num)






