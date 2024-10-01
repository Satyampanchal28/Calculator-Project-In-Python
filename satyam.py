#  calculator
# functions for operations
# user input
# print result

# function to add  number

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def add(num1,num2):
    return num1 * num2

def add(num1,num2):
    return num1 / num2

def add(num1,num2):
    return (num1 + num2)/2

print("ples select a opertion:\n " "1. additon\n " \
      "1.addition\n"\
        "2.substraction\n"\
          "3.multiplication\n"\
              "4.division\n"\
                 "5.avreage\n")

select = int(input("select a operation from 1,2,3,4,5:"))

numbe1= int(input("enter first number"))
numbe2= int(input("enter second number"))

if select == 1:
    print(numbe1, "+", numbe2, "= ", \
          add(numbe1,numbe2))
          
if select == 2:
    print(numbe1, "_", numbe2, "= ", \
          add(numbe1,numbe2))
                    
elif select == 3:
    print(numbe1, "*", numbe2, "= ", \
          add(numbe1,numbe2))
    
elif select == 4:
    print(numbe1, "/", numbe2, "= ", \
          add(numbe1,numbe2))
    
if select == 5:
    print("(",numbe1, "+", numbe2,")", "= ", "/", "2", "=" ,\
          add(numbe1,numbe2))
                    
     
else:
    print("invalid opretion! pls select again! ") 
    

 

 
 
