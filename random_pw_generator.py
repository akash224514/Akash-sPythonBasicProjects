#Random Password Generator
'''
1)Take lenght of password as a input from user
2)declare string of characters
3)using random.sample function generate random string 
4)print random string

'''
import random
import sys
print("****Random password generator****\n")
pslen=int(input("Enter password length: "))

ran_str="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

x=" ".join(random.sample(ran_str,pslen))

print(f"Password generated as: {x}")