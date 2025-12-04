integers = []

ints = int(input("Input the integers you want to put: "))
for i in range(1, ints + 1):
    integers.append(i)

even_numbers = 0
for i in integers:
    if i % 2 == 0:
        even_numbers += 1
print(f"Even Values: {even_numbers}")