''''
17. **Checking for Armstrong Numbers in a Range**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, Number Theory  
    **Description**: Write a program to find all Armstrong numbers within a given range.  
    **Example**:  
    Input: `range = [1, 500]`  
    Output: `[1, 153, 370, 371, 407]`  
    Explanation: Armstrong numbers between 1 and 500 are 1, 153, 370, 371, and 407. 

'''
def checkarmstrongnum(limit):
    armstrong_list = []

    for num in range(1,limit+1):
        power = len(str(num))  
        total =0

        for digit in str(num):
            total += int(digit)**power
        if total ==num:
            armstrong_list.append(num)
    return armstrong_list 

print("Armstrong numbers from 1 to 500:", checkarmstrongnum(500))





