# 가장 큰 수를 K번 더하고 두번째로 큰 수를 한 번 더하는 연산을 반복
# n,m,k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split()) 
# input()으로 입력받은 문자열을 split()을 이용해 공백으로 나눈 리스트로 바꾼 뒤에, map을 이용하여
# 해당 리스트의 모든 원소에 int()함수를 적용한다.
# 최종적으로 그 결과를 list()로 다시 바꿈으로써 입력받은 문자열을 띄어쓰기로 구분하여
# 각각 숫자 자료형으로 저장하게 되는것이다.
data = list(map(int, input().split()))
result = 0
data.sort() # 입력 받은 수를 내림차순으로 정렬

first = data[n-1] # 가장 큰수
second = data[n-2] # 두 번째로 큰수

# 가장 큰수가 더해지는 횟수 계산
count = int ( m // (k+1) * k + m % (k+1))

result = 0
result += count * first
result += (m-count) * second

print(result)