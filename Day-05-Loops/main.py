#For Loop statement
for i in range(0, 5):
    print(i)
#Output:
0
1
2
3
4


#While loop statement
number = 31
power = 1

while power <= number:
    power *= 2
print(power)

#Output
32


#Break Statement (breaking buddy)
for i in range(11):
    if i == 5:
        break
    print(i)

#Output
0
1
2
3
4

#Continue Statement (skipping buddy)
for i in range(0, 10):
    if i%2 != 0:
        continue
    print(i)

#Output
0
2
4
6
8


#Range() with step count
start = int(input()) #1
end = int(input()) #10
step = int(input()) #2

for i in range(start, end, step):
    print(i)

#Output:
1
3
5
7
9


#Nested loop

# Outer loop
for i in range(3):
    print(f"Outer loop: {i}")
    
    # Inner loop
    for j in range(2):
        print(f"  Inner loop: {j}")

#Output
Outer loop: 0
  Inner loop: 0
  Inner loop: 1
Outer loop: 1
  Inner loop: 0
  Inner loop: 1
Outer loop: 2
  Inner loop: 0
  Inner loop: 1
