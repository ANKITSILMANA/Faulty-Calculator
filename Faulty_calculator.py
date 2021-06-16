#oper=("+","-","*","/")
inp1=int(input("Enter 1st Number"))
inp2=int(input("Enter 2nd Number" ))
inp=input("Enter Operator")
if inp=="+":
    if (inp1 == 56) or (inp2 == 9):
        print(77)
    else:
        add = inp1 + inp2
        print(add)
elif inp=="-":
    sub = inp1 - inp2
    print(sub)
elif inp=="*":
    if (inp1 == 45) or (inp2 == 3):
        print(555)
    else:
        mul = inp1 + inp2
        print(mul)
elif inp=="/":
    if (inp1 == 56) or (inp2 == 6):
        print(4)
    else:
        div = inp1 / inp2
        print(div)
else:
    print("Invalid Operator")
