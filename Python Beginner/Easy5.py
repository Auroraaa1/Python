numbers = []
for i in range(1, 6):
    number = int(input(f"Enter a integer {i}: "))
    numbers.append(number)
print(f"Sum of the numbers: {sum(numbers)}")