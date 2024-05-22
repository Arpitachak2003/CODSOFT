print("simple calculator")

num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
print("press 1 for addition")
print("press 2 for substraction")
print("press 3 for multiplication")
print("press 4 for substraction")

choice=int(input("enter your choice from 1-4:"))

if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1/num2)
else:
    print("invalid input")
