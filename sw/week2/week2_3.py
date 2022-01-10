#3 회전 
from collections import deque

T = int(input())
for i in range(1, T+1):
  N, M = map(int, input().split())
  q = deque(list(map(int, input().split())))
  for j in range(M):
    q.append(q.popleft()) # 왼쪽에서 빼낸 것(popleft)을 마지막에 append로 더함
  print(f'#{i} {q[0]}')