N = int(input())

crimes_lis = input().split()
crimes_lis = list(map(int, crimes_lis))


heired = 0
untreated = 0

for i in range(N):
    if crimes_lis[i] == abs(crimes_lis[i]):
        heired += crimes_lis[i]
        continue
    if heired > 0 and crimes_lis[i] != abs(crimes_lis[i]):
        heired -= 1
        continue
    if heired == 0 and crimes_lis[i] != abs(crimes_lis[i]):
        untreated += 1

print(untreated)