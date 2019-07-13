'''
Created on Oct 25, 2018

@author: Abhishek.kumar
'''


# Function for Getting the operator, Num1, Num2
def Get_Expression():
    Num1 = 0
    Num2 = 0
    Operator = ""
    Op_Index = 0

    # Getting the operator using operator Index
    for operation in exp:
        if operation in operation_list:
            Op_Index = exp.index(operation)
            Operator = exp[Op_Index]

            '''
            If the Operator string is of two char
            e.g. 5**5
            Entered expression: ['5', '*', '*', '5'] >> will change in['5', '**', '5']
            str.isdigit() -> Return true if all characters in the string are digits and there is at least one character,false otherwise.
            '''
            try:
                if (exp[Op_Index + 1] == Operator) and ((exp[Op_Index + 2]).isdigit()):
                    exp[Op_Index] += exp[Op_Index + 1]
                    exp.remove(exp[Op_Index + 1])
                Operator = exp[Op_Index]
            except IndexError:
                exit('Input the last Numbers !!!')

    # Returning the values to handel invalid input
    if Operator == (exp[0] or exp[-1]):
        exit('Input both the Numbers !!!')
    elif not any(Operator == i for i in operation_list):
        exit('Invalid input for operator value !!!')

    # Getting the 1st number
    for i in range(Op_Index):
        Num1 = str(Num1)
        Num1 += str(exp[i])

    # Getting the 2nd number
    for i in range(Op_Index, (len(exp) - 1)):
        Num2 = str(Num2)
        Num2 += str(exp[i + 1])
    try:
        Num1 = float(Num1)
        Num2 = float(Num2)
        return Num1, Num2, Operator
    except:
        exit('Operation unsupported or invalid !!!')


# Main calling function
operation_list = ["**", "/", "//", "%", "*", "+", "-"]
# Getting Input from User
exp = list(input("Enter the expression : \n"))
if len(exp)==0:exit('Empty Input !!!')
Num1, Num2, Operator = Get_Expression()

# Division by 0 Exception Handler:
if any(Operator == j for j in operation_list[1:4]) and Num2 == 0:
    try:
        Num1 / Num2
    except ZeroDivisionError:
        exit("ZeroDivisionError: Oops!!! can't divide by zero")
if Operator == "**":
    Result = Num1 ** Num2
    print(Num2, "Exponent of", Num1, "is:", Result)
elif Operator == "/":
    Result = Num1 / Num2
    print("Division of numbers is:", Result)
elif Operator == "//":
    Result = Num1 // Num2
    print("Floor_Division of numbers is:", Result)
elif Operator == "%":
    Result = Num1 % Num2
    print("Modulo of numbers is:", Result)
elif Operator == "*":
    Result = Num1 * Num2
    print("Multiplication of numbers is:", Result)
elif Operator == "+":
    Result = Num1 + Num2
    print("Sum of numbers is :", Result)
elif Operator == "-":
    Result = Num1 - Num2
    print("Difference of numbers is:", Result)
else:
    print("Invalid input. Please check again!!!")