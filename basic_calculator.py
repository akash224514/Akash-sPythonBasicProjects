#Basic calculator program using Python

'''
1)Take input from user about which operation they want to perfrom
2)Take two numbers from user
3)Perform respective operation
'''
print("***Basic Calculator***")
a=int(input(f"Enter First number: "))
b=int(input(f"Enter Second number: "))

print("1.Add\t2.Subtract\t3.Multiply\t4.Divide")
ch=int(input("Please select operation: "))



def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

if ch==1:
        print(a,"+",b,"=",add(a,b))
   
if ch==2:

        print(a,"-",b,"=",sub(a,b))
    

if ch==3:
        res=a*b
        print(a,"*",b,"=",mul(a,b))
    

if ch==4:
        res=a/b
        print(a,"/",b,"=",div(a,b))
    
   
