#Python Binary search
'''
1)Declare a list of numbers
2)sort the list
3)check weather it is present in the middle or not
4)if not then check at front
5)if not then check at rear
'''

li=[1,3,2,4,5,6,9,8,7,10]
li.sort()
print(f"Final list of elements is: {li}")
st=0
lst=len(li)-1
mid=(st+lst)//2

found=False

item=int(input("Enter the number you want to search: "))
print(f"Entered number is: {item}")


while(st<=lst and not found):
    mid=(st+lst)//2
    if li[mid]==item:
        print(f"Number is found at position: {mid}")
        found=True
    else:
        if item < li[mid]:
            lst=mid-1
        else:
            st=mid+1

if found==False:
    print("Number is not present in list")
