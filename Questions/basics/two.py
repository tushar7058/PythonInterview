

N = int(input("Enter a Num :"))
def tablesno(N):
    for i in  range(1,11):
        if i<10:
            print(i*N,end=" ")
        else:
            print(i*N)   
tablesno(N)