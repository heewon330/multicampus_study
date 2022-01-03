#5 지그재그 숫자
n=int(input())
#sum=0
for i in range(1,n+1):
  num=int(input())
  sum=0
  for j in range(1,num+1):
    if j % 2 ==0:
      sum-=j
    else:
      sum+=j
  print(f'#{i} {sum}')