'''Given a list of numbers. Determine the element in the list with the largest value. Print the value of the largest 
element and then the index number. If the highest element is not unique, print the index of the first instance.'''

a = input()
b = a.split()

for i in range(len(b)):
    b[i] = int(b[i])
max_a = max(b)
print(max_a)

for i in range(len(b)):
    
    if b[i] == max_a:
        print(i)
        break