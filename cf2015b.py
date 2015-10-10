N = int(raw_input())
A = map(int, raw_input().split())
tmp = 0

for i in range(N):
    tmp = tmp + A[i]*(2**(N-i-1))

print tmp
