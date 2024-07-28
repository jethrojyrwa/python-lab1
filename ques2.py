#Lab exercise 1: question 2

A = ['abc','xyz','aba','1221']

for i in range(len(A)):
    s = A[i]
    if s[0] == s[-1]:
        print(s)
