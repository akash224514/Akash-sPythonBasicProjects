#GUESS THE NUMBER
'''
1)Generate a random number
2)Take the number as a input from user
3)Give three chances to user
4)Compare random number generated and user inputed number
5)Print the result

'''

import random
print("***GUESS THE NUMBER***")

g_num=random.randint(1,10)
cnt=3
for i in range(0,3):
    user_Inp=int(input("Guess the number please:    "))

    if user_Inp==g_num:
        print("Bravo!! you guessed it right!")
        print(f"You guessed the number right and number was {g_num}")
        exit()
    else:
        print("OOPS! Try again!!")
        cnt=cnt-1
        print(f"Chances remaining {cnt}")
        while cnt==0:
            print("Chances Exhausted ! Exiting...")
            exit()

