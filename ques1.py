#Lab Exercise 1: question 1

L = [-2,4,6,2,3] #declaring a python list with numeric values
s = 0 #initialising sum
m = 1 #initialising product

#(a) finding the sum of all elements
for i in range(len(L)):
    s = s + L[i]

print("Sum of all the items in the list: ",s)

#(b) finding the product of all elements
for i in range(len(L)):
    m = m * L[i]
print("Product of all the items: ",m)

#(c) finding the largest
lar=L[0]
for i in range(1,len(L)):
    if L[i]>lar:
        lar = L[i]

print("Largest element: ",lar)

#(d) finding the smallest
sma=L[0]
for i in range(1,len(L)):
    if L[i]<sma:
        sma = L[i]
        
print("Smallest element: ",sma)
