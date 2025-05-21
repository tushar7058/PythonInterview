'''
16. **Finding the Sum of Elements in an Array**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, Arrays  
    **Description**: Write a program to find the sum of elements in an array.  
    **Example**:  
    Input: `array = [1, 2, 3, 4, 5]`  
    Output: `15`  
    Explanation: The sum of the elements in the array is 15.  

'''
arr = [1, 2, 3, 4, 5]
def sumelmentarray(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum = sum+arr[i]
        i+=1
    print("sum of all element is :",sum)

sumelmentarray(arr)

