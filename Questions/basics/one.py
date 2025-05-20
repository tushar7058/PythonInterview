# while loop
count  = 0
while(count<10):
    count = count+1
    print("the Count is :",count)
else:
    print("In else block")


list = [1,2,3,4,5]
for i in list:
    print(i)

list1 = [1,2,3,4,5]
for i in range(len(list1)):
    print(i)
print('\n')
for i in list1:
    print(i)

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

for letter in 'geeksforgeeks':
    if letter == 'e' and letter =='s':
        continue
    print('current letter :',letter)