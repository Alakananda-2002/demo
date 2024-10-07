 #Python program to determine whether the given year is a leap year or not. 
x=int(input("enter the year"))
print(x)
if (x%4==0) and (x%100!=4) or (x%400==0):
    print("leap year")
else:
    print("not leap year")


# demo
