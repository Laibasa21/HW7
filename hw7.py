#Laiba Sabahat HW #7 10/30/22 (CHAPTER 8)

#1: DQ 1
    #a. Definite loop is a loop that runs the code for a specific number of times.
        #An indefinite loop keeps running until it finds some condition to stop running. 
    #b. A for loop is used when the number of iterations is predefined.
        #A while loop does not have a predefined number of iterations. 
    #c. interactive loops are loops which interact with the user to determine how many times it needs to be repeated. 
        #A sentinel loop keeps going until it is told to stop. 
    #d. A sentinel loops keeps repeating until it is promoted to stop.
        #An end-of-file loop terminates when it detects the end of a file. It is also known as EOF. 

#2: DQ 2
    #a. P: T,T,F,F  Q: T,F,T,F  PandQ: T,F,F,F  Not(PandQ): F,T,T,T
    #b. P: T,T,F,F  Q: T,F,T,F  notP: F,F,T,T   Not(P)andQ: F,F,T,F
    #c. P: T,T,F,F  Q: T,F,T,F  NotP: F,F,T,T   NotQ: F,T,F,T   NotP,NotQ: F,T,T,T
    #d. P: T,T,T,T,F,F,F,F   Q: T,T,F,F,T,T,F,F     R: T,F,T,F,T,F,T,F  PandQ: T,T,F,F,F,F,F,F      PandQorR: T,T,T,F,T,F,T,F

#3: DQ 3s,c
    #a. code
#n=int(input("Enter value for n: "))
#i=1
#total=0
#while(i<=n):
#    total +=i
#    i+=1
#print(total)
#print()

    #c. code
#n=int(input("Enter value for n: "))
#total=0
#while(n!=999):
#    total +=n
#    n=int(input("Enter value for n: "))
#print(total)
#print()

#4: PE 1
#def Fibonacci(n):
#    if n<0:
#        print("Incorrect input")
#    elif n==0:
#        return 0
#    elif n==1:
#        return 1
#    else:
#        return Fibonacci(n-1)/Fibonacci(n-2)
#print(Fibonacci(10))

#5: PE 4
def syr(x):
    l=[]
    l.append(x)
    while x!=1:
        if x%2==0:
            x=int(x/2)
        else:
            x= (3*x)+1
        l.append(x)
    print(l)
syr(5)

#6: 
