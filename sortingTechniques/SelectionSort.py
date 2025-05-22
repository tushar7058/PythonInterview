'''

Selection Sort is a comparison-based sorting algorithm. 
It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.
This process continues until the entire array is sorted.

1.First we find the smallest element and swap it with the first element. 
This way we get the smallest element at its correct position.
2.Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
3.We keep doing this until we get all elements moved to correct position.

'''

def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                # update min_idx if a smaller element is found
                min_idx = j

        arr[i],arr[min_idx ]= arr[min_idx],arr[i]

def printarray(arr):
    for val in arr:
        print(val,end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    print("Original array:",end="")
    printarray(arr)
    selectionsort(arr)
    print("Sorted array:",end="")
    print(arr)