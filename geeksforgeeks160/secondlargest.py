'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
Note: The second largest element should not be equal to the largest element.

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34


Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.

Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.

'''
class solution: 
    def secondlargest(self,arr):
        n = len(arr)
        largest = -1
        secondlargest  = -1
        for i in range(n):
            if arr[i]>largest:
                secondlargest = largest
                largest = arr[i]
            elif arr[i]<largest and arr[i]>secondlargest:
                secondlargest = arr[i]
        return secondlargest
c = solution()
result = c.secondlargest(arr=[12, 35, 1, 10, 34, 1])
print("Second largest No:",result)