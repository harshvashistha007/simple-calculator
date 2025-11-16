a=int(input("enter first"))
b=int(input("enter any second"))

choice=input("enter you choice +,-,*,/")

if choice=="+":
    print(a+b)
elif choice=="-":
    print(a-b)
elif choice=="/":
    print(a/b)
elif choice=="*":
    print(a*b)
else:
    print("invalid")

