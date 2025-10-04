'''

31. **Generating a Pascal’s Triangle**  
    **Difficulty**: Medium  
    **Topics**: Arrays, Mathematical Computations  
    **Description**: Write a program to generate Pascal's Triangle up to a given number of rows.  
    **Example**:  
    Input: `rows = 4`  
    Output:  
    ```
    1  
    1 1  
    1 2 1  
    1 3 3 1  
    ```  
    Explanation: Pascal's Triangle with 4 rows is generated.  


'''

n= 4
def pascalTriangel(n):
    for i in range(n):
        num=1
        row = []
        for j in range(i+1):
            row.append(num)
            num = num*(i-j)//(j+1)
        print(" ".join(map(str,row)))

pascalTriangel(n)

    