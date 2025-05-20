'''

6. **Identifying Palindromes**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, String Manipulation  
   **Description**: Write a program to check if a string or number is a palindrome.  
   **Example**:  
   Input: `string = "radar"`  
   Output: `Palindrome`  
   Explanation: "radar" reads the same backward as forward.  

'''
def is_palindrome(value):
    # Convert the input to string and lowercase it for case-insensitive comparison
    str_value = str(value).lower()
    # Remove spaces (optional, if you want to ignore them)
    str_value = str_value.replace(" ", "")
    # Check if string is equal to its reverse
    return str_value == str_value[::-1]
 
# Main program
user_input = input("Enter a string or number to check for palindrome: ")

# Try to convert input to an integer if possible
try:
    value = int(user_input)
except ValueError:
    value = user_input  # keep it as string if not a number

# Check palindrome
if is_palindrome(value):
    print("✅ It is a palindrome.")
else:
    print("❌ It is NOT a palindrome.")