'''

You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.

Example 1:

Input:
str = catinahat
Output:
True
Explanation:
cat and hat both are present
1 number of times.


Example 2:

Input:
str = bazingaa
Output:
True
Explanation:
cat and hat both are present
0 number of times.


Constraints:
1 <= str.size() <= 105

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

'''

def cat_hat(str):

    cat_count =0
    hat_count = 0

    for i in range (len(str)-2): 
        sub = str[i:i+3]
        if sub =='cat':
            cat_count+=1
        elif sub=='hat':
            hat_count+=1       
    return cat_count == hat_count
        