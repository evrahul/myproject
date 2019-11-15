print("welcome to my calculator")
print("press any number from 1 to 4 ")
print ("To ADD press:1\n"
       "To sub press: 2\n"
       "To mul press:3\n"
       "To div press: 4")
a=int(input("enter your choice"))
if a==1:
    b=int(input("enter any number"))
    c=int(input("enter any number"))
    d=b+c
    print ("sum=%d"%(d))
elif a==2:
    b = int(input("enter any number"))
    c = int(input("enter any number"))
    d = b - c
    print ("sum=%d"%(d))
elif a==3:
    b = int(input("enter any number"))
    c = int(input("enter any number"))
    d = b * c
    print ("mul=%d"%(d))
elif a==4:
    b = int(input("enter any number"))
    c = int(input("enter any number"))
    d = b / c
    print ("div=%d"%(d))

else:
    print ("wrong input")

