# Function to calculate the factorial
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result

# Input from the user
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")
