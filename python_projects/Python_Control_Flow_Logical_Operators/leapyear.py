print("Leap Year")
print("-----------")

#year is divisible by 4 
    # then check whether year is divisble by 100 if it is not divisible by 100 then it is leap year
    #if it is divisible by 100 then check whether if it is divisible by 400 
        #if it is divisble is  divisible by 400 then it is leap year
        # if it is not divisible by 400 then it is not leap year
#year is not divisible by 4 it is not leap year
enter_year=input("Enter year: ")
if enter_year.isdigit():#checking it is int
    year_val=int(enter_year)#converting into int
    
    len_year=len(enter_year)#checking length
    if len_year==4:#checking 4 digit number
        div_four= year_val%4 #year is divisible by 4
       # print(div_four)
        if div_four==0:
            div_hund=year_val%100
            #print(enter_year, " is a Leap Year")
                
                
            #print(div_hund)
            if div_hund!=0:
                print(enter_year, " is a Leap Year")
            else:
                div_fhun=year_val%400
                if div_fhun==0:
                    print(enter_year, " is  a Leap Year")
                else:
                    print(enter_year, " is not a Leap Year")
             
        else:
            print(enter_year, " is not a Leap Year")
    else:
        print("Enter a 4 digit number")
else:
    print("Entered value is not number")