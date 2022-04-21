print("Even or Odd Number")
print('------------------')
num= int(input("Enter a number : ")) 
val=num%2 # checking the number by dividing by 2 ,if it is getting remainder 1 it is odd or not getting remainder it is even
if val == 0:
    print("Entered value is Even Number")
else:
    print("ENtered value is Odd Number")