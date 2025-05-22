'''
 
2.	Write a function to find the factorial of a number using recursion.

'''

num = int(input("Enter a num:"))
def factorialNo(num):
    if num<0:
        return 
    elif num==0 or  num==1:
        return 1
    else:
        return num*factorialNo(num-1)

print(factorialNo(num))


