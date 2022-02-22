print("Enter Two Numbers: ", end="")
num1 = int(input())
num2 = int(input())
print("Enter the Operator (+,-,*,/): ", end="")
operator = input()
if operator == '+':
    def add(num1, num2):
        return (num1+num2)
    temp = add(num1,num2)
    print (temp)
elif operator == '-':
    def sub(num1, num2):
        return (num1-num2)
    temp = sub(num1,num2)
    print (temp)
elif operator == '*':
    def mul(num1,num2):
        return (num1*num2)
    temp = mul(num1,num2)
    print (temp)
elif operator == '/':
    def div(num1,num2):
        return (num1/num2)
    temp = div(num1,num2)
    print (temp)
else:
    print ("it is not a valid option Altered")
