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

#Arguments:
def is_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

for i in range(15, 34):
    is_even(i)
for i in range(153, 219):
    is_even(i)
