n = int(input())

bags = [500, 100, 50, 10, 5, 1]
change = 1000 - n
count = 0

for bag in bags:
    count += change // bag
    change %= bag
    
print(count)
