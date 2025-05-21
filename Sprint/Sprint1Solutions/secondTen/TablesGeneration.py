'''
18. **Generating Multiplication Tables**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, Mathematical Computations  
    **Description**: Write a program to generate multiplication tables for a given number.  
    **Example**:  
    Input: `number = 4`  
    Output:  
    ```
    4 x 1 = 4  
    4 x 2 = 8  
    4 x 3 = 12  
    4 x 4 = 16  
    4 x 5 = 20  
    ```  
    Explanation: The multiplication table for 4 up to 5 is generated.  
'''
num = int(input("enter a num to generate Table :"))
def generateTable(num):
    for i in range(1,11):
        table = i*num
        print(f"{num}*{i}={table}")

generateTable(num)