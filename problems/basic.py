#power() 함수 작성하기
def power(n):
  return 2**n

print(power(9))

#n ^ m 구하기
n=3
m=4
result=1
for i in range(1,m+1):
    result *= n

print(result)


#러시아 농부의 곱셈
n=123
m=12
sum=0
while n>0:
  #print(n,'X',m)
  if n%2==1:
    sum+=m
  n=n//2
  m=m*2

print(sum)


#팩토리얼 구하기
n=5
result=1
for i in range(1,n+1):
  result *= i

print(result)


#유클리드 호제법
def gcd(a,b):
    if b > a:
        a, b = b, a
    n=a%b
    if n == 0:
        return b
    else:
        return gcd(b, n)
print(gcd(12,16))


#피보나치 수- 리스트 이용
n=int(input())
def fib(num):
    f=[0,1]
    for i in range(2,num+1):
        f.append(f[i-2]+f[i-1])
    return f[num]

print(fib(n))