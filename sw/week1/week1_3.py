#3 평균값 구하기
n=int(input())
for i in range(1,n+1):
  num=list(map(int,input().split()))
  avg=sum(num)/len(num)
  print(f'#{i} ',round(avg))