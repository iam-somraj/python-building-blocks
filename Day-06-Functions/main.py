def hello_function():
    print("Hello World!")

n = int(input())

for i in range(n):
    hello_function()

#Input:
6

#Output:
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!

#--------------------------------------------------------

no_of = int(input())

def cal_sol():
    sum = 0
    for i in range(1, 10001):
        sum += i
    print(sum)

for i in range(no_of):
    cal_sol()

#Input:
4

#Output:
50005000
50005000
50005000
50005000

#--------------------------------------------------------

#Argument:
def mult(a, b):
    print(a * b)

a = int(input())
b = int(input())
mult(a, b)

#Input:
4
5

#Output:
20

#-------------------------------------------------------

def calculate_area(length, width):
    print(length * width)

length = float(input())
width = float(input())

calculate_area(length, width)

#Input:
4
5

#Output:
15.0

#-----------------------------------------------------

#Returns
def square_num(n):
    return n * n

num = int(input())

result = square_num(num)
print(result)

#Input:
6

#Output:
36

