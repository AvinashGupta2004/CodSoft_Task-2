"__________________________________________CODSOFT INTERNSHIP PROGRAM 2023______________________________________________________"
"_________________________________________PROJECT: SIMPLE BASIC CALCULATOR______________________________________________"
"____________________________________PROJECT PREPARED AND DESIGNED BY AVINASH GUPTA_____________________________________________"
print("Welcome to Mini Calculator")
while True:
    print("""Options:
        1. Adding two numbers.
        2. Subtraction of two numbers.
        3. Product of two numbers.
        4. Division of two Numbers.
        5. Square of any Numbers.
        6. Base to the power raised.""")
    userInput = int(input("Enter the Desired Operation: "))
    if userInput==1:
        a,b = eval(input('Enter the Numbers separated by Commas: '))
        print("The result of the Operation was: "+str(a+b))
    elif userInput==2:
        a,b = eval(input('Enter the Numbers separated by Commas: '))
        print("The result of the Operation was: "+str(a-b))
    elif userInput==3:
        a,b = eval(input('Enter the Numbers separated by Commas: '))
        print("The result of the Operation was: "+str(a*b))
    elif userInput ==4:
        a = eval(input('Enter the Dividend of the operation: '))
        b = eval(input('Enter the divisor of the operation: '))
        print("The result of the given operation is: "+str(a/b))
    elif userInput==5:
        a= eval(input('Enter the Number whose square is to be finded: '))
        print("The result of the Operation was: "+str(a**2))
    else:
        a = eval(input('Enter the Base number of the Operation: '))
        b = eval(input("Enter the Power/Index of the operation: "))
        print("The result of the Operation was: "+str(a**b))

    userInput = input("Do you want to continue with the program?(y/n): ")
    if userInput=="y":
        print("=============================================================")
        continue
    else:
        print("Thank You. Visit again!")
        break
    

    
