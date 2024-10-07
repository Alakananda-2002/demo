# Create a function that checks whether a given number is prime or not. 
# Return True if it's prime, otherwise False 
def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
           count+=1
        if count==2:
            print("true")
        else:
            print("false")
prime(4)