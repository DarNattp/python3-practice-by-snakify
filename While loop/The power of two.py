'''For a given integer N, find the greatest integer x where 2x is less than 
or equal to N. Print the exponent value and the result of the expression 2x.
Don't use the operation **.'''

# Read an integer:
a = int(input())
x = 1
zong = 2
while zong <= a:
    zong *= 2
    x += 1
print(x-1, zong//2)
