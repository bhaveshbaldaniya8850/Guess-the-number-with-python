import random
p = "y"
b=5
while(p =="y"):
    a = random.randint(1,100)
    for i in range(b):
        x = str(i+1)
        g = int(input("Enter your "+x+" guess number :"))
        if(g<0 & g>100):
            print("Enter valid input from 1...100")
            break
        elif (g==a):
            print("Congratulations your guess is right")
            a=1
            break
        elif(g>a):
            print("your ",g," is grater than the real number")
        elif(g<a):
            print("your ",g," is lesser than the real number")
        if((i==b-1) and (a!=g)):
            print("batter luck next time")
            print("your hidden number is ",a)
        if(i==b-1):
            print ("do you want to play it again   Y/N")
            p = str(input())
