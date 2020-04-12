a = input().split(' ')
print(a)
count = {}
for i in a:
    if i not in  count.keys():
        count[i] += 1
    else:
        count[i] = 0
print(count)