n, k = map(int, input().split())
count = 0

# 만약에 나누어 지면 나누고 아니면 1을 뺀다.
# 이건 한가지 케이스도 더 생각해야한다!
while n >= k:
    if( n == 1 ):
        break

    if ( n % k != 0):
        n -= 1
        count += 1
    
    n //= k
    count += 1

while n > 1:
    n-=1
    count+=1
    
print(count)
    
