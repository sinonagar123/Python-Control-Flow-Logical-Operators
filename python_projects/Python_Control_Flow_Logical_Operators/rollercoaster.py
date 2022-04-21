print("Welcome to ROller coaster Ride")
print("------------------------------")
height_p=input("Enter your height in cm: ") #getting height
if height_p.isdigit(): # checking it is digit
    height_int=int(height_p) #converting into int
    if height_int >=120: #checking height is > 120
        print("Welcome to ROller Coster Ride. YOu are eligible to ride")
        age=int(input("Enter your age: "))
        
        if age<=12:#checking age 
            
                   # print("5$ ")
            age_val=5
        elif age >12 and age <=18:
            age_val=7
        else:
            age_val=12
        ticket=input("Do you want to take photo Y or N: ")
        ticket_len=len(ticket)
        ticket_val=0
        if ticket_len ==1 and ticket=='y' or ticket =='Y' or ticket=='n' or ticket=='N':
            if ticket =='Y' or ticket=='y':
                ticket_val=3
                age_val=age_val+ticket_val
            
                
            print("Total amt",age_val)
                
            
                
        else:
            print("Please enter Y or N")
            
        
    else:
        print("Sorry, YOu are not eligible to ride")
else:
    print("Height should enter in digts")