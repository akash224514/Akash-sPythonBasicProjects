#DICE ROLL SIMULATOR
'''
1)Give User options
2)Take User input
3)By choice generate a random number
4)exit

'''
import random

while True:
    print("******WELCOME TO DICE ROLL SIMULATOR*********")
    print("What you would like to do?")
    print("1.Dice a roll    2.Exit")
    user=int(input("Enter your choice: "))
    if user==1:
        print(random.randint(1,6))
    else:
        print("Exiting....")
        exit()
