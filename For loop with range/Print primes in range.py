'''Statement
A prime number is a natural number greater than 1 that has no positive divisors 
other than 1 and itself. Given two integers A and B, print all prime numbers between them, inclusively.'''

lower = int(input())
upper = int(input())



for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
    #xxx