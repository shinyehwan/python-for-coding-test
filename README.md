# python-for-coding-test
## 천천히 꾸준히
일일일알!
```
n,m,k = list(map(int, input().split()))
import sys
변수 = sys.stdin.readline()
```

```
# 스텍 개념 이해
print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
```

```
# 큐 개념 이해
from collections import deque
# Queue 구현을 위해 deque 라이브러리 사용
queue = deque()
print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```

```
- 재귀함수는 종료 조건을 꼭 명시해줘야함.(if문 사용)
- 재귀함수는 스택 자료구조와 동일함.
- 반복문 대신에 재귀 함수를 사용했을 때 얻을 수 있는 장점은 무엇일까? -> 반복문을 이용하는 것과 비교했을 때 더욱 간결하다.
```

