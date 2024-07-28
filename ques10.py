#Lab exercise 1: question 10

months = ['January','February','March','April','May','June','July','August',
          'September','October','November','December']

m = input("Enter the month name:")

if(m in (months[0],months[2],months[4],months[6],months[7],months[9],months[11])):
    print("The number of days in",m,"is: 31")

elif(m in (months[3],months[5],months[8],months[10])):
    print("The number of days in",m,"is: 30")

elif(m in months[1]):
    y = int(input("Enter the year: "))
    if(y%4==0):
        print("The number of days in February is: 29")
    else:
        print("The number of days in February is: 28")
else:
    print("Incorrect Month Name/Invalid Input")
    
    
