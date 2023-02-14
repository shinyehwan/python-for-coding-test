n = int(input())
result = 0

while n >= 3:
    if(n % 5 == 0):
        result += n // 5
        break
    
    n -= 3
    result += 1

if( n == 1 ):
    print(-1)

else:
    print(result)    




