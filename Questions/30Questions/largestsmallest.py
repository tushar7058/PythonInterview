'''

Write a program to find the largest and smallest elements in a list.

'''

class solution:
    def smallest(self, arr):
        n  = len(arr)
        arr.sort()
        for i in range(n):
            return arr[0]
        
    def largest(self, arr):
        n = len(arr)
        arr.sort()
        for i in range(n):
            return arr[-1]

# object creation    
c = solution()
result = c.smallest(arr=[2,5,3,6])
print("smallest element :",result)




