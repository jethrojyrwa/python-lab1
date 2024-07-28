#Lab exercise 1: ques4

ListColour = [["Black","Red","Maroon","Yellow"],["000000","FF0000","800000","FFFFF00"]]
output = []

colourNames = ListColour[0]
colourCodes = ListColour[1]
              
for i in range(len(colourNames)):
        output.append({'colorName':colourNames[i],'colorCode':colourCodes[i]})
        
print(output)        

               
