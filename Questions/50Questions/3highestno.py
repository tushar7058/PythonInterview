'''
15 min : 

list = [1,2,3,4,5]
return 3rd higest num

a = [2,3,4,5]
ans= 4

- common things
    1. list
    2. integer
    3. collection
    4. set -> output
    5. Sorted 

a = [22,37,51,76,95]
ans = 51


- take first value
- check value 
- ascending/sort set values
- list calling
- compare all with other nums

'''

list  = [51,76, 37,22,95]
maxele = list[0]
for i  in range(1 ,len(list)):
    if (list[i]>maxele):
        maxele = list[i]
print("MaxElement is :",maxele)


# # with the help functions
# def thirdhigest(list):
#     list.sort()
#     print('third large elements',list[-1])

# thirdhigest(list)

    


