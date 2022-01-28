n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)] # 캐릭터가 이동할 수 있는 맵(좌표)
array = [] # 바다 육지를 구분할 수 있는 맵 (바꿀수 없는 입력할 때 정해지는 배열)
d[x][y] = 1 # 처음 좌표 방문 한 것으로 표기
count = 1
turn_time = 0

for i in range(n) : # n행만큼 배열을 추가 한다는 거겠지
    array.append(list(map(int, input().split())))
# 북 동 남 서(0, 1, 2, 3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 이미 캐릭터가 방문한 곳이라고 표기해줘야함 꼭
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue # 밑에 코드는 볼 필요 없다
    else :
        turn_time += 1

        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if array[nx][ny] == 0:
                x = nx
                y = ny
            else :
                break
            turn_time = 0 # 다시 0으로 초기화하는 작업을 꼭 해줘야함
print(count)
    
            

        
