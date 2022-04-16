def calc(num1,num2):

    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

    operation = int(input('Choose which operation would you like to perform: '))

    if operation==1:
        print(num1+num2)
    if operation==2:
        print(num1-num2)
    if operation==3:
        print(num1*num2)
    if operation==4:
        print(num1/num2)
