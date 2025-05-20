'''

#  Print All Natural Numbers

Input: 5

Output:

1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
1 + 2 + 3 + 4 + 5 = 15


'''
a = int(input("Enter a Num :"))
def natural(a):
    sum =0
    for i in range(1, a+1):
        sum +=i
        print(i ,'sum is :', sum)
natural(a)