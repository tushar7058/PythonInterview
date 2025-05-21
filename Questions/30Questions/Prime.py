'''
1. Write a program to check whether a number is prime or not.
n = 10
1 , 3 , 5 , 7  -> prime numbers
sum = 16

'''

num = int(input('Enter an Num :'))
def checkprime(num):
    if num<=1:
        print("not a prime number")
        return 

    for i in range(2,num):
        if num % i == 0:
            print('num is  not prime ')
            return
    print('num is  prime')


checkprime(num)



