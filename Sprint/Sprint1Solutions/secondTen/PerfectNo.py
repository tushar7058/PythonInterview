'''

20. **Checking for Perfect Numbers**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, Number Theory  
    **Description**: Write a program to determine if a number is a perfect number.  
    **Example**:  
    Input: `number = 28`  
    Output: `Perfect Number`  
    Explanation: 28 is a perfect number because its divisors (1, 2, 4, 7, 14) sum up to 28.


'''
# Input from user
def perfectNo(num):
    if num <=1:
        return False
    sum_of_divisior = 1
    for i in range(2,num):
        if num%i == 0:
            sum_of_divisior += i
    return sum_of_divisior ==num
try:
    number = int(input("Enter a number to check if it's a Perfect Number: "))
    if perfectNo(number):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
except ValueError:
    print("Please enter a valid integer.")




    