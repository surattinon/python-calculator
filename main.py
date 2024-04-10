# Add your functions here!
def divide(user_input1, user_input2):
    print(user_input1 / user_input2)

def add(user_input1, user_input2):
    print(user_input1 + user_input2)

def subtract(user_input1, user_input2):
    print(user_input1 - user_input2)

def multiply(user_input1, user_input2):
    print(user_input1 / user_input2)

def modulo(user_input1, user_input2):
    print(user_input1 % user_input2)

def main():
    print("Enter the operation you want to perform: ")

# From basu02 branch
print("From branch \"basu02\"")
a = 55
b = 48
a + b = c
print(c)

# From basu branch commit 2
print("From branch \"basu commit 02\"")
d = 10
e = 45
d + e = f
print(f)

# From basu02 branch commit 03
print("From branch \"basu02\"")
a = 55
b = 48
a + b = c
print(c)

    user_operation = input()
    user_input1 = int(input("Enter the first number: "))
    user_input2 = int(input("Enter the second number: "))

    if user_operation == "add":
        add(user_input1, user_input2)
    elif user_operation == "subtract":
        subtract(user_input1, user_input2)
    elif user_operation == "multiply":
        multiply(user_input1, user_input2)
    elif user_operation == "divide":
        divide(user_input1, user_input2)
    elif user_operation == "modulo":
        modulo(user_input1, user_input2)


main()
