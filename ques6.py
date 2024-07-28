#question 6

num = int(input("Enter a number: "))

#sum of digits
temp = num
s = 0

while(temp>0):
    d = temp % 10
    s = s + d
    temp = temp//10

print("Sum of the digits in",num,"is",s)


#reverse of the num
temp = num
rev = 0

while(temp>0):
    d = temp % 10
    rev = (rev*10) + d
    temp = temp//10


print("Reverse of",num,"is",rev)
