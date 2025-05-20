'''

15. **Sorting an Array**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, Sorting Algorithms  
    **Description**: Write a program to sort an array of numbers in ascending order.  
    **Example**:  
    Input: `array = [3, 1, 4, 1, 5, 9]`  
    Output: `[1, 1, 3, 4, 5, 9]`  
    Explanation: The array sorted in ascending order is [1, 1, 3, 4, 5, 9]. 


'''

arr= [1,2,3,4,5]
def sortArray(arr):
    for i in range(0,len(arr)-1):
        for j in range (i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i] ,arr[j] = arr[j] ,arr[i]
    # print sorted array
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

sortArray(arr)
