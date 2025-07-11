#Arithmetic Operators
a = 6
b = 2
c = a+b
c1 = a-b
c2 = a*b
c3 = a/b

print(f"a = {a}, b = {b}, c = {c}, c1 = {c1}, c2 = {c2}, c3 = {c3}");

#Output:
8, 4, 12, 3.0

#-----------------------------------------------------------------------------------

# Modulo Operator
a = 9
b = a%2

print(f"a = {a}")
print(f"b = {b}")

#Output:
a = 9
b = 1

#------------------------------------------------------------------------------------

#Arithmetic Shortcuts
c = 4
c *= 2
c -= 1 

print(f"c = {c}")

#Output:
c = 7

#------------------------------------------------------------------------------------

#Comparison Operators
n1 = 8
n2 = 9
n3 = n1==n2
n4 = n1!=n2
n5 = n1>n2
n6 = n1<n2
n7 = n1>=n2
n8 = n1<=n2

print(f"n3 = {n3}, n4 = {n4}, n5 = {n5}, n6 = {n6}, n7 = {n7}, n8 = {n8}")

#Output:
n3 = False, n4 = True, n5 = False, n6 = True, n7 = False, n8 = True

#---------------------------------------------------------------------------------------

#Logical Operators
age = 18
has_identity = True

result = age >= 18 and has_identity
result1 = age >= 18 or has_identity
result2 = age >= 18 and not has_identity
#In Python, the "not" operator should come before the variable, and you need "and" to connect the conditions.

print("Can entry:", result)
print("Can entry:", result1)
print("Can entry:", result2)

#Output:
Can entry: True
Can entry: True
Can entry: False

#---------------------------------------------------------------------------------------

#Logical Operators with Truth Table references
a = True
b = True
c = False

d = a and b and (not c)
print(f"d = {d}")

#Output:
d = True
