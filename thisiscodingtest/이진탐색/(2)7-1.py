

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

n = int(input_data[0])
target = input_data[1]


def seq_search(n, array, target):
    for i in range(n):
        if array[i] == target:
            return i+1


print(seq_search(n, array, target))