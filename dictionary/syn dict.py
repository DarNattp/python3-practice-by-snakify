dic = {}
for i in range(int(input())):
    word, syn = input().split()
    dic[word] = syn
print(dic[input()])