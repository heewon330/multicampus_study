#4 간단한 소인수분해
n=int(input())
a=0; b=0; c=0; d=0; e=0

for i in range(1,n+1):
  num=int(input())
  while num !=1:
    if num%2==0:
      a+=1
      num=num/2
    if num%3==0:
      b+=1
      num=num/3
    if num%5==0:
      c+=1
      num=num/5
    if num%7==0:
      d+=1
      num=num/7
    if num%11==0:
      e+=1
      num=num/11

  print(f'#{i} {a} {b} {c} {d} {e}')