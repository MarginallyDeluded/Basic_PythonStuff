
num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))
operation = input('Enter the mathematical operation to perform: ')

if operation == '*':
    ans = num1*num2
elif operation == '/':
    if num2 == 0:
        print('mathematical error! process exited')
        exit()
    ans = num1/num2
elif operation == '+':
    ans = num1+num2
elif operation == '-':
    ans = num1-num2
else:
    print('Enter any one of these operations (+,/,-,*)')
    exit()

answer = f'{num1} {operation} {num2} = {ans}'
print(answer)
