 #Write a lambda function to check if a given string is a palindrome.
# def pal():
#     

x=input("enter the string")
#reverstr=x[::-1]
a=lambda y:y[::-1]
y=a(x)
if y==x:
    print("palindrome")
else:
    print("not palindrome")