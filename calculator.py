while True:
 print("\n\n################")
 print("CLI Calculator")
 print("################\n")

 print("1.Add")
 print("2.Substract")
 print("3.Multiply")
 print("4.Divide")
 operator = input("Enter the operator: ")

 def Add():
     num1 = int(input("Enter the first digit: "))
     num2 = int(input("Enter the second digit: "))
     sum = num1 + num2
     print("\033[91mThe answer is: \033[0m",sum)
     

 def Substract():
     num1 = int(input("Enter the first digit: "))
     num2 = int(input("Enter the second digit: "))
     diff = num1 - num2
     print("\033[91mThe answer is: \033[0m",diff)

 def Multiply():
     num1 = int(input("Enter the first digit: "))
     num2 = int(input("Enter the second digit: "))
     prod = num1 * num2
     print("\033[91mThe answer is: \033[0m",prod)

 def Divide():
     num1 = int(input("Enter the first digit: "))
     num2 = int(input("Enter the second digit: "))
     div = num1 / num2
     print("\033[91mThe answer is: \033[0m",div)

 if operator == "1":
     Add()
 elif operator == "2":
    Substract()
 elif operator == "3":
    Multiply()
 elif operator == "4":
    Divide()
 else:
    print("\033[91mInvalid Input Entered!\033[0m")
    
