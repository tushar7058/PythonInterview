# python lamda function

a = int(input("enter value of a :"))
b = int(input("enter a value of b:"))
def add(a,b):
   print("sum of a and b is :",a+b)

# add(a,b)


# above function with lamda
sum = lambda x , y : x+y
print(sum(3,5))