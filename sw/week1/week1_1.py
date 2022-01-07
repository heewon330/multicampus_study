T = int(input())
for t in range(1, T + 1):
  num = list(map(int, input().split()))
  sum=0
  for i in num:
    if i%2 != 0:
      sum+=i
  print('#{} {}'.format(t, sum))