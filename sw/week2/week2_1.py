#1 숫자추가
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())			# 수열의 길이, 추가 횟수, 출력할 인덱스 번호
    num = list(map(int, input().split()))		# 수열
    for _ in range(M) :
        idx, n = map(int, input().split())		# 추가할 인덱스와 숫자 정보
        num.insert(idx, n)
    print(f"#{test_case} {num[L]}")