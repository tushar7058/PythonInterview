'''

- Second Largest Element 

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.

Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

'''
a = []
def secondlarges(a):
    
   n = len(a)

   largest = -1
   secondlargest = -1

   for i in range (len(a)):

      if a[i]>largest:
         secondlargest = largest
         largest = a[i]
      
      elif a[i]>secondlargest and a[i]!=largest:
         secondlargest = a[i]

   return secondlargest