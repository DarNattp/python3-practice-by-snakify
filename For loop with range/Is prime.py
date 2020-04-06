'''A prime number is a natural number greater than 1 that has no 
positive divisors other than 1 and itself. Given an integer N > 1, print PRIME if it's prime and print COMPOSITE otherwise.
'''

a = int(input())

for i in range(2, a+1):
    if a % i == 0 and a != i:
        print('COMPOSITE')
        break
    elif a % i == 0:
        print('PRIME')
        break