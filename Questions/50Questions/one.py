'''
#  check no is even or odd

- take input from user and check no is even or odd.
- no is 0 then return -> not even not odd
- write function for these.


'''
def checkNo(a):
    if a%2==0:
        print('No is even')
    else:
        print('No is Odd')

checkNo(13)


# Using lambda Function
a = [1, 2, 3, 4, 5]
res = map(lambda num: str(num) + " Even" 
          if num % 2 == 0 else str(num) + " Odd", a)
print("\n".join(res))