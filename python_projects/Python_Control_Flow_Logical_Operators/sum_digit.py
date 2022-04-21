print("Sum of a 4 digit number")
i=0
sum=0

num=input("Enter a 4 digit number: ")
strlen=len(num)
if strlen==4:
  
  for i in range(i,4,1):
   sum=sum+int(num[i])
  print("Sum of ",num," is ",sum)

else:
  print("The number you entered is not a 4 digit number")
  h=0
  