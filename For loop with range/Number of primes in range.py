'''
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given two integers A and B, 
print the number of primes between them, inclusively.
'''

a = int(input())
b = int(input())
count = 0
for i in range(a, b+1):
    true_prime = True
    
    for num in range(2, i):
        if i % num == 0:
            true_prime = False
    if true_prime:
        count += 1

print(count)