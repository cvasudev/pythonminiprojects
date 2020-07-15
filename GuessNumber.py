import random

#variable that will store the value for random number
rannum = random.randrange(1,10,1)

flag=True

name = input("Please enter your name : ")

while(flag):
   try:
       print(f"Hi {name}") 
       num = int(input("Please guess the number in the range 1-10 : "))
       if num not in range(1,11) and num!=12:
           print("Incorrect Value")
       elif num == rannum:
           print("The number is correct !!!")
           flag=False
       elif num>rannum and (num-rannum)>3:
           print("Number is too much greater")
       elif num>rannum and (num-rannum)<=3:
           print("The number is greater however you are very close!!!")
       elif num<rannum and (rannum-num)>3:
           print("Number is too much less")
       elif num<rannum and (rannum-num)<=3:
           print("The number is less however you are very close!!!")
       elif num==12:
           break
   except:
       print("Invalid entry!!!")
    
        

        
              
    
