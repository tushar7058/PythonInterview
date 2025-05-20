'''

input :
a = "ABCDEF"

output :
a -> "FEDCBA"

s = 5
s-i-1 

for 0 => 5-0-1=  4
fof 1 => 5-1-1 = 3
for 2 => 5-2-1 = 2
for 3 => 5-3-1 = 1
for 4 => 5-4-1 = 0

'''
class ReverseMain:
    # for loop
    def reverse_string_for(self, s):
        reversed_char = ""
        for char in s:
            reversed_char = char + reversed_char  # Prepend each character
        return reversed_char    

    # while loop
    def reverse_string_while(self, s):
        reverse_string = ""
        i = len(s) - 1
        while i >= 0:
            reverse_string += s[i]
            i -= 1
        return reverse_string

    # Two pointer approach
    def reverse_string_two_pointer(self, s):
        s_list = list(s)  # Convert string to list
        left, right = 0, len(s_list) - 1
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return ''.join(s_list)  # Convert back list to string

s = ReverseMain()
print(s.reverse_string_two_pointer("Good"))       # Output: dooG
print(s.reverse_string_while("hello"))           # Output: olleh
print(s.reverse_string_for("Morning"))           # Output: gninroM