import sys

t=int(input())

for i in range(0, t):
    n,s,e,k = map(int, input().split())
    N=[0 for j in range(n)]
    N = list(map(int, input().split()))
    N2=[]
    1
    for j2 in range(s-1, e):
        N2.append(N[j2])
    
    N2.sort()
    #print(N2)

    print(N2[k-1])


    
