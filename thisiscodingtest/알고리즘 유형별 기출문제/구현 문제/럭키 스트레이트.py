# TypeError: 'float' object cannot be interpreted as an integer
# range 안에는 정수만 들어와야 하므로 //를 사용한다.
# TypeError: unsupported operand type(s) for +=: 'int' and 'str'
# int와 str 값을 더할 수 없어서 int(n[i]) 감싸준다.
# IndexError: string index out of range
# 인덱스는 범위에 주의한다. or i in range(length//2, length): ...


n = input()

length = len(n)

result1 = 0
result2 = 0

for i in range(length//2):
    result1 += int(n[i])

for i in range(length//2, length):
    result2 += int(n[i])

if(result1 == result2):
    print('LUCKY')
else:
    print('READY')

    