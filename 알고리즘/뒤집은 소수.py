import sys

N = int(input()) #N개의 자연수 입력

arr = [0 for i in range(N)]

arr = list(map(int, input().split()))

#숫자 뒤집기
def reverse(x):
    x2=""
    while x > 0:
        if x%10 > 0 :
            x2+=str(x%10)
            x=x//10
        else:
            x=x//10
    return x2

#소수인지 확인하는 함수
def isPrime(x):
    cnt=0
    flag = True
    for i in range(2, x+1):
        if x%i == 0 :
            cnt+=1
            if cnt >= 2 and i < x :
                flag = False
                break
    
    return flag
    

arr2 = []
for i in arr:
    result = reverse(i)

    result2 = isPrime(int(result))

    if result2 :
        arr2.append(result)

print(arr2)


