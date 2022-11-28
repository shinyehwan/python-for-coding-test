n =  int(input())
times = list(map(int, input().split()))

times.sort()
sum = 0
prev = 0

for time in times:
    sum += prev + time
    prev += time

print(sum)



