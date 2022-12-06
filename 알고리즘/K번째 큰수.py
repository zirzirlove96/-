import sys

N,K=map(int, input().split())

N2=[0 for i in range(N)]
N2=list(map(int, input().split())) #array에 입력

N2.sort(reverse=True)

N3=[]

#print(N2)

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            N3.append(N2[i]+N2[j]+N2[k])

#중복된 값 제거
"""
for i in my_list:
    if i not in result:
"""
N4 = list(set(N3)) #중복된 값 제거

#내림차순
N4.sort(reverse=True)
print(N4)
print(N4[K-1])