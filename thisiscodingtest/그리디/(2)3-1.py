n = 1260
coins = [500, 100, 50, 10]
result = 0

for coin in coins:
     result += n // coin
     n %= coin

print(result)