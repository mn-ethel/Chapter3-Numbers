T=int(input("Enter a number"))
if T==0:
    print("The factorial of 0 is 1")
else:
    factorial =1
    for i in range(1,T+1):
        factorial = factorial*i
        print("The factorial of" , T ,"is", factorial)