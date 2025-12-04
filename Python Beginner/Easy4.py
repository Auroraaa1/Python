#Easy4.py
def max_of_two(a, b):
    maximum = max(a, b)
    return maximum
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
result = max_of_two(first, second)
print("The maximum is:", result)