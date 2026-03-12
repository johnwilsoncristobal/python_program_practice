# Input two numbers
number1=float(input("Enter a number: "))
number2=float(input("Enter another number: "))

# Check if which number is bigger or both number are equal
if number1 > number2:
    print("Number 1 is bigger")
elif number2 > number1:
    print("Number 2 is bigger")
else:
    print("Both numbers are equal")