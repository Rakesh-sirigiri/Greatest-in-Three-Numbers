a = int(input("enter first:"))
b = int(input("enter second:"))
c = int(input("enter third:"))
if a>b:
    if a>c:
        print("the greatest is:",a)
    else:
        print("the greatest is:",c)
else:
    if b>c:
        print("the greatest is:",b)
    else:
        print("the greatest is:",c)
