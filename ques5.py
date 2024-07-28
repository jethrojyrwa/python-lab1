#Lab exercise 1: question 5

#5(a)
print("All even numbers between 1 and 50 and their squares")
for i in range(1,50):
    if i%2==0:
       print(i,"^2 = ",i**2)

print("\nAll even numbers between 1 and 100 and their squares")
for i in range(1,100):
    if i%2==0:
       print(i,"^2 = ",i**2)
