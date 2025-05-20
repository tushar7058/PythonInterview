'''

7. **Crafting Star Patterns**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Patterns  
   **Description**: Write a program to create different star patterns (e.g., pyramid, diamond).  
   **Example**:  
   Input: `patternType = "pyramid", height = 5`  
   Output:  
   ```
       *
      ***
     *****
    *******
   *********
   ```  
   Explanation: A pyramid pattern with a height of 5 is generated.


'''
height = 5
def starpattern(height):
    # Top half of the diamond
    for  i in range(height):
        spaces = ' '*(height-i-1)
        star = '*'*(2*i+1)
        print(spaces+star)
    # Bottom half of the diamond
    for i in range(height - 2, -1, -1):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

starpattern(height)
    

     


