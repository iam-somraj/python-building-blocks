Operators are used to perform the operations on values.

First we will discuss the most basic arithmetic operators, they may be familiar from past math classes.

1. Arithmetic Operators

Addtion: +
Subtraction: -
Multiplication: *
Division: /
--------------------------------------------------------------------------------------------------------
2. Modulo Operator

Modulo: %

# "/" tells us the reminder of the division whereas "/" tells us the result of the division
--------------------------------------------------------------------------------------------------------
Tip 1: Arithmetic Shortcuts

Python created a cool shortcut for self-arithmetic operations.

For example, instead of writing:
a = 5
a = a + 5 # a = 10 now

We can simplify it by writing +=:
a = 5
a += 5 #a = 10 now
--------------------------------------------------------------------------------------------------------
3. Comparison Operators

Equal: ==
Not Equal: !=
Greater Than: >
Less Than: <
Greater Than or Equal: >=
Less Than or Equal: <=
--------------------------------------------------------------------------------------------------------

4. Logical Operators

Logical operators are used to combine the conditional statements.

Python has three logical operators:

a. and
The "and" operator returns True if both statements are true.

b. or
The "or" operator returns True if at least one statement is true.

c. not
The "not" operator returns True if the statement is false, and False if the statement is true.
--------------------------------------------------------------------------------------------------------

5. Logical Operators with Truth Table

Logical operators have a special table called "Truth table" that shows what the combination of logical operators returns.

and
a - False, False, True, True
b - False, True, False, True
a & b - False, False, False, True

or
a - False, False, True, True
b - False, True, False, True
a & b - False, True, True, True

not
a - True 
not a - False
b - False
not b - True
