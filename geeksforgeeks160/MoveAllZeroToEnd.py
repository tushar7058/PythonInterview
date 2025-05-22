'''

You are given an array arr[] of non-negative integers. 
Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements.
The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.


Input: arr[] =  [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105

'''


# def moveallZeroToEnd(arr):
#     arr1 =[]
#     for i in range (0,len(arr)):
#         if arr[i] == 0:
#             arr1.append(arr[i])
#         for j in range(0,len(arr)):
#             if arr[i]!=0:
#                 arr1.append(arr[i])
#     return arr1
                    
# moveallZeroToEnd(arr)

arr = [1, 2, 0, 4, 3, 0, 5, 0]
def moveAllZeroToEnd1(arr):
    n = len(arr)
    count = 0
    # traverse
    for i in range(n):
        if arr[i]!=0:
            arr[count] = arr[i]
            count+=1
        # fill remaning positon with 0
    while count<n:
        arr[count] = 0
        count+=1
    return arr
print(moveAllZeroToEnd1(arr))


# Using extra space
def moveAllZeroToEnd(arr):
    result = []
    # Step 1: Add all non-zero elements
    for num in arr:
        if num != 0:
            result.append(num)
    # Step 2: Count zeros
    zero_count = arr.count(0)
    # Step 3: Add zeros at the end
    result.extend([0] * zero_count)
    return result