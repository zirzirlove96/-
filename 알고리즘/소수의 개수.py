import sys

N = int(input())

#1초 제한시간을 넘길 것 같음 
"""cnt = 0
cnt2 = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i%j == 0:
            cnt+=1
    if 2 <= cnt < 3 :
        cnt2+=1

print(cnt2)    
"""
cnt = 0
arr = [0 for i in range(N+1)]

#에라토스테네스 체 = 채로 걸러내는 방식 
#배열로 2의 배수, 3의 배수에 1을 넣어 소수를 걸러낸다.
for i in range(2, N+1):
    if arr[i] == 0:
        cnt+=1
        for j in range(i,N+1,i):
            arr[j]=1

print(cnt)