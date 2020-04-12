a = int(input())
b = int(input())
c = int(input())

if a-b != 0 and a*b - c > 0:    
    print('YES') if ((a*b) - c) % b == 0 or ((a*b) - c) % a == 0 else print('NO')
    #print(c%(a-b))
elif a == b == c:
    print('YES')
else:
    print('NO')