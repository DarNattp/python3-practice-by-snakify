res = 0

for i in range(1, int(input())+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    res += fact
print(res)