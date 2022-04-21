
#WAP TO FIND SUM OF ALL CONSECUTIVE ODD NUMBERS FROM 1 TO 10
sum=0
for i in range(1,11):
  if(i%2!=0):
     sum=sum+i
print("The sum of consecutive odd numbers from 1 to 10:",sum)
i=i+1