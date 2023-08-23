import math

operator_list = ['+','-','*','/','^','√']

print("Calculator\n")

while True:                                     #A loop until the user want to close the program
    print("Supported operators: ", end='')
    print(operator_list)
    print("Input 'exit' to exit.")
    print("Which operation you want to do?")

    while True:                 #A loop until the user enters a valid operator
        operation = input("")
        if operation == 'exit':
            print("See you soon!")
            exit()
        elif operation in operator_list:
            break
        else:
            print("You must enter a valid operator!")

    while True:             #A loop to handle errors
        try:
            if operation == '√':                        #The root needs one number so it is seperated from other operations
                num = float(input("Enter a number: "))
                result = math.sqrt(num)
                print("√"+str(num)+" = "+str(result)+'\n')
            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if operation == '+':
                    result = num1+num2
                elif operation == '-':
                    result = num1-num2
                elif operation == '*':
                    result = num1*num2
                elif operation == '/':
                    result = num1/num2
                else:
                    result = math.pow(num1,num2)
                print(str(num1)+' '+ operation +' '+str(num2)+' = '+str(result)+"\n")

            break           #To break the loop if there is not any errors
        except ValueError:
            print("Error: Invalid input. You must enter a valid number!\n")       #If the user do not inputs a float or integer
        except ZeroDivisionError:
            print("Error: Zero division of a number is undefined.\n")  #The result is undefined, user got informed
            break                                               #Then break the loop

