# 알파벳인지 아닌지 확인하는 isalpha() 라는 메소드가 있잖아??
# [0, 2, 3, 5, 6] 12
# 첫번째, 이해하기 쉬운 숫자부터 보면, 알파벳이 아닐때, 첫번째 길이의 인덱스(자릿수)(몇 번째)(i)가 아닌 n이라는 문자열에 해당하는 인덱스에(자릿수) 해당값(n[i])을 넣어 줘야 한다. 
# 두번째, 문자열의 배열이 나오는게 아닌 문자열의 자리에 해당하는 인덱스가 소팅 되었다.
# ['a', 'b', 'c', 'k', 'k'] 13
# 배열, 리스트를 문자열로 바꿔주는 메소드 answer = ''.join(result)
# TypeError: can only concatenate str (not "int") to str
# 정수 값을 문자열로 바꿔줘야 한다.
# value = str(value)

n = input()
result = []
value = 0

for i in range(len(n)):
    if(n[i].isalpha()):
        result.append(n[i])
    else:
        value += int(n[i])

result.sort()

answer = ''.join(result)
value = str(value)
print(answer+value)

