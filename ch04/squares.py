squares=[]
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

squares = [value ** 2 for value in range(1,11)]
print(squares)

total=0
for value in range(1,1000001):
    total+=value
print(total)

for value in range(1,20,2):
    print(value)

for value in range(3,31,3):
    print(value)

cubes=[value ** 3 for value in range(1,11)]
print(cubes)