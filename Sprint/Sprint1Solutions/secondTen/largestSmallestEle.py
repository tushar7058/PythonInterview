'''

14. **Finding the Largest and Smallest Numbers in an Array**  
    **Difficulty**: Easy  
    **Topics**: Basic Programming, Arrays  
    **Description**: Write a program to find the largest and smallest numbers in an array.  
    **Example**:  
    Input: `array = [4, 7, 1, 8, 5]`  
    Output: `Largest: 8, Smallest: 1`  

    Explanation: The largest number in the array is 8 and the smallest is 1.  



arr = [1,2,3,4]
       i  j
       i>j
       j =i
       
'''
arr = [3,4,5,2]
def twopointerMethod1(arr):
    if len(arr)==0:
        return
    
    left ,right =0 ,len(arr)-1
    min_val = max_val = arr[0]

    while(left<=right):
        min_val = min(min_val,arr[left],arr[right])
        max_val = max(max_val,arr[left],arr[right])
        left+=1
        right-=1

    print(f" Minvalue:{min_val},Maxvalue:{max_val}")

twopointerMethod1(arr)

# through sort method
def sortmethod(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i] , arr[j] = arr[j] ,arr[i]        
    # to print array
    for i in range(n):
        print(arr[i],end=" ")
    print()

# def main():
#     arr = [1,2,3,4,5]
#     sortmethod(arr)
#     print(f"Smallest:{arr[0]},largest:{arr[-1]}")
# if __name__ =="__main__":
#     main()








        
