num=int(input("Enter a number:"))
print("Factorial of " + str(num))
fact=1
for i in range(1,num+1):
  fact=fact*i
print(fact)
i=i+1