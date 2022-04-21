print("Welcome to python pizza")
print("-----------------------")
print("Small size (s) : 15$ \nMedium size (m) : 20$ \nLarge size (l) : 25$ ")
size=input("Select Your Pizza size s,m or l: ")
pep =input("Add Pepproni for $2 y or n: ")
cheese =input("Add cheese for $1 y or n: ")
pep_len=len(pep)
size_len=len(size)
cheese_len=len(cheese)
pizzaamt=0
peramt=0
cheeseamt=0
tot_amt=0
if size_len==1 and size=='S' or size=='s' or size =='l' or size=='L' or size=='m' or size=='M':
    if size=='s' or size =='S':
        pizzaamt=15
    if size=='m' or size=='M':
        pizzaamt=20
    if size=='l' or size=='L':
        pizzaamt=25
    if pep_len==1 and pep=='y' or pep=='Y' or pep=='n' or pep=='N':
        if pep=='y' or pep=='Y':
            
            peramt=2
    if cheese_len==1 and cheese=='y' or cheese=='Y' or cheese=='n' or cheese=='N':
        if cheese=='y' or cheese=='Y':
            
            cheeseamt=1
    tot_amt=tot_amt+pizzaamt+peramt+cheeseamt
    print("Total Amount: ",tot_amt)
else:
    print("Please choose current pizza size s, m or l ")
    