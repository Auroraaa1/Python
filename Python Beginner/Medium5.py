Students = []

for i in range(1,4):
    Name = input(f"Enter student name {i}: ")
    Students.append(Name)

print("Student list: ")
for a in Students:
    print(a)

name1 = input ("Enter a student to remove: ")

if name1 in Students:
    Students.remove(name1)
    print("Updated student list: ")
    for a in Students:
        print(a)

else:
    print("Student not found.")