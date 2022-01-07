T= int(input())

for t in range(1, T+1):
    d = list(input())
    N = len(d)
    stack = []
    for i in range(N):
        #stack이 비었거나, 스택의 마지막 값이 데이터 내 값과 같지 않은 경우 
        #=> stack에 저장(append)
        if not stack or stack[-1] != d[i]:
            stack.append(d[i])
        #stack에 값이 있고, 스택의 마지막 값과 데이터 내 값과 같은 경우 
        #=> stack에서 제거(pop)
        elif stack and stack[-1] == d[i]:
            stack.pop()
    print(f'#{t} {len(stack)}')