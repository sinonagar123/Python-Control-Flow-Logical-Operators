print("Sum of two digit number")
print("-----------------------")
val=input("Enter two digit number: ") # entered number will be in string
num_len=len(val) # checking the length of the string
sum=0
if val.isdigit(): # checking user entered value is digit or string 
   # print("User input is number ")
    if num_len == 2: # checking 2 digit
         
        sum=int(val[0])+int(val[1]) # adding the numbers
        print("Sum of " ,val ," is ",sum)
    else:
        print("User input is not 2 digit")
else:
    print("User input is not number")
