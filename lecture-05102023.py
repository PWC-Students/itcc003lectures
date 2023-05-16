# # Python Programming - 05/10/2023 Lecture
# Repetitive Control Structure
# var = 1
# isOnUse = True
#
# while isOnUse:
#     # Ask the first number from the user
#     firstNum = float(input("Enter the first number:"))
# #     Ask the second number from the user
#     secondNum = float(input("Enter the second number:"))
#     operator = input("Enter the operation you wanted to use: (+, -, x, /, modulo):")
#
#     if operator == "+":
#         result = firstNum + secondNum
#     elif operator == "-":
#         result = firstNum - secondNum
#     elif operator == "x":
#         result = firstNum * secondNum
#     elif operator == "/":
#         result = firstNum / secondNum
#     elif operator.lower() == "modulo":
#         result = firstNum % secondNum
#     else:
#         print("Please enter a valid operation to use")
#         continue
#
#     print("The result is", result)
#
#     anotherOperation = input("Perform another operation? (y/n):")
#     if anotherOperation.lower() == "y":
#         isOnUse = True
#     if anotherOperation.lower() == "n":
#         isOnUse = False
#         break
#     else:
#         isOnUse = False
#         print("Exiting Loop")
#         break
# Introduction to Functions
# A function is a way to organize your code and repetitive blocks of code.
# Reusable codes use functions most of the time.
customerOrder = ["burger", "fries", "milktea"]
print(customerOrder)
orderToVoid = input("What order would you like to void?: [1, 2, 3]")
isVoid = False
# Arguments and Parameters
# Parameter accepts values passed onto a specific function
def voidOrder(voidThisOrder):
    if voidThisOrder == "1":
        customerOrder[0] = ""
    elif voidThisOrder == "2":
        customerOrder[1] = ""
    elif voidThisOrder == "3":
        customerOrder[2] = ""
    isVoid = True
    return isVoid
# Argument is the value passed when calling a function
if voidOrder(orderToVoid):
    print("Successfully removed order!")
    print(customerOrder)