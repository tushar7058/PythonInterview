'''

Given an array arr and an integer k. You have to find the maximum product of k contiguous elements in the array. 

Questions:

Input: arr[] = [1, 2, 3, 4] and k = 2
Output: 12 
Explanation: The sub-array of size 2 will be 3 4 and the product is 12.

Input: arr[] = [1, 6, 7, 8] and k = 3
Output: 336
Explanation: The sub-array of size 3 will be 6 7 8 and the product is 336.

Expected Time Complexity: O(n)
Expected Auxilary Space: O(1)

Constraints:
1 <= arr.size() <= 106
1 <= k<= 8
1<= arr[i] <=102

'''

class solution:
    def findmaxprod(self, arr,k):
        n = len(arr)
        if k>n:
            return None
        # initial product for firt windo
        maxprod = currprod = 1
        for i in range (k):
            currprod*=arr[i]
            maxprod = currprod
        # slide the window
        for i  in range (k,n):
            # avoid zero division
            currprod = currprod // arr[i-k]*arr[i]
            maxprod = max(maxprod,currprod)
        return maxprod


s = solution()
print(s.findmaxprod([1,2,3,4],2))




        