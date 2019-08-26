## Problem 1:
#Create a function that will ask the user for a number. Use the function to get two numbers from the user, then pass the two numbers to a function. Add, subtract, multiple, and divide the numbers.
# !! : "Create a function that will ask the user for a number" This function should only ask the user for one number then be called twice 
def ask(): # this function ask for 2 inputs puts input into num function call
    userInput = int(input("enter a number "))
    userInput2 = int(input("enter another number "))
    num(userInput, userInput2)
def num(num1, num2): # this function uses input from ask function and then prints the add, subtract, multiply , and division of  it
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

ask()