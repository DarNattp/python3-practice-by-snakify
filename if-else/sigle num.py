n = 2
while n != 1 and n!= 4:
    if len(str(n)) == 2 or len(str(n)) == 1:
    
        
        first = n // 10
        sec = n % 10

        n = first**2 + sec**2
    elif len(str(n)) == 3:
    

        first = n // 100
        mid = n%100 // 10
        sec = n%10

        n = first**2 + mid**2 + sec**2

print(n)