#Python program to implement Rock Paper Scissor game
'''
Winning Rules as follows :

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.

'''

from ctypes.wintypes import PINT
from multiprocessing import parent_process
import random
from unittest import result

print("***Rock-Paper-Scissor***")
print("Winning Rules as follows:\nRock vs paper=paper wins\nRock vs scissor=Rock wins\npaper vs scissor=scissor wins.")

print("\nchoices are:\n1.Rock\n2.Paper\n3.Scissor")
usr_choice=int(input("Enter your choice: "))

while usr_choice >3 or usr_choice<0:
    print("Invalid choice!")
    exit()

if usr_choice==1:
    print("User's choice is: Rock")
    ch_name="Rock"

if usr_choice==2:
    print("User's choice is: Paper")
    ch_name="Paper"

if usr_choice==3:
    print("User's choice is:Scissor")
    ch_name="Scissor"
print("\nNow its computer's turn..")

rand_int=random.randint(1,3)

print(f"Computer's choice is: {rand_int}")

if rand_int==1:
    print("Computer's choice is: Rock")
    rand_ch="Rock"

elif rand_int==2:
    print("Computer's choice is: Paper")
    rand_ch="Paper"
else:
    print("Computer's choice is: Scissor")
    rand_ch="Scissor"

result=""

print(f"\nIts {ch_name} vs {rand_ch}!!")

if((usr_choice==1 and rand_int==2) or (usr_choice==2 and rand_int==1)):
    print("Paper wins!")
    result="Paper"


elif((usr_choice==2 and rand_int==3) or (usr_choice==3 and rand_int==2)):
    print("Scissor wins!")
    result="Scissor"

elif((usr_choice==3 and rand_int==1) or (usr_choice==1 and rand_int==3)):
    print("Rock wins!")
    result="Rock"

else:
    print("No result....")
    exit()


if result==ch_name:
    print("\ni.e.User wins!")
else:
    print("\ni.e.Comp wins!")
