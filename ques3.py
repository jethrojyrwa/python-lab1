#lab exercise 1: question 3

#pattern 1
L = ['A','B','C','D','E']

for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    k=0
    for j in range(i+1):
        print(L[k]," ",end="")
        k = k+1
    print()

#pattern 2
print()
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
