'''

12. **Counting Vowels and Consonants in a String**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, String Manipulation  
    **Description**: Write a program to count vowels and consonants in a given string.  
    **Example**:  
    Input: `string = "hello world"`  
    Output: `Vowels: 3, Consonants: 7`  
    Explanation: "hello world" contains 3 vowels (e, o, o) and 7 consonants (h, l, l, w, r, l, d).  
    
'''

def checkConstantandvowels(str):
    vowels = "aeiou"
    vowel_count = 0
    constant_count  = 0
    for char in str.lower():
        if char.isalpha(): # check if the character is a letetr
            if char in vowels:
                vowel_count+=1
            else:
                constant_count+=1
    return vowel_count, constant_count

str = "hello world"
vowels,constant = checkConstantandvowels(str)
print(f"Vowels:{vowels},Constants:{constant}")


