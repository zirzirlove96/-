import sys

N = int(input())

cnt = 0
cnt2 = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i%j == 0:
            cnt+=1
    if 2 <= cnt < 3 :
        cnt2+=1

print(cnt2)    