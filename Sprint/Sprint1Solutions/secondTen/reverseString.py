'''

13. **Reversing a String**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, String Manipulation  
    **Description**: Write a program to reverse a given string.  
    **Example**:  
    Input: `string = "programming"`  
    Output: `"gnimmargorp"`  
    Explanation: The reversed string of "programming" is "gnimmargorp".  

'''
str = 'abcs'
def reversestring(str):
    reverse_string = ''
    for char in str:
        reverse_string = char+reverse_string # -> 1.a , 2.ba , 3.cba , 4. scba
    return reverse_string

print(reversestring(str))

s = 'abcsd'
print(s[::-1])