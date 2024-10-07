#Create a function that takes a string as input and returns the number of vowels in the string
a="a","e","i","o","u","A","E","I","O","U"
b=input("enter the string")
def vowels(x):
    count=0
    #a=input("enter the string")
    for i in a:
        if i in b:
            count+=1
    print(count)
        #count+=1
vowels(b)