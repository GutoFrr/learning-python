# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print("The result for " + str(a) + " + " +
          str(b) + " is = " + str(answer) + "\n")


def subtract(a, b):
    answer = a - b
    print("The result for " + str(a) + " - " +
          str(b) + " is = " + str(answer) + "\n")


def multiply(a, b):
    answer = a * b
    print("The result for " + str(a) + " * " +
          str(b) + " is = " + str(answer) + "\n")


def divide(a, b):
    answer = a / b
    print("The result for " + str(a) + " / " +
          str(b) + " is = " + str(answer) + "\n")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        print()
        add(a, b)

    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        print()
        subtract(a, b)

    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        print()
        multiply(a, b)

    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        print()
        divide(a, b)

    elif choice == "e" or choice == "E":
        print("Program finished")
        quit()
