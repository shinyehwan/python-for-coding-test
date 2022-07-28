# 역슬래쉬를 쓸 때에는 \\ 하나 더 붙인다.
# '를 출력해야할 땐 "로 문자열을 표현

# print('\\    /\\')
# print(" )  ( ')")
# print('(  /  )')
# print('\\(__)|')


# 9498
# score = int(input())

# if ( 90 <= score <=100):
#     print('A')
# elif (80 <= score <90):
#     print('B')
# elif(70<= score < 80):
#     print('C')
# elif(60<= score <70):
#     print('D')
# else:
#     print('F')

# 2739
# n = int(input())

# for i in range(1,10):
#     print(n, '*', i, '=', n * i)

# 10430
# A,B,C = map(int, input().split())

# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

# 2438
n = int(input())

for i in range(1, n+1):
    print('*' * i)

    