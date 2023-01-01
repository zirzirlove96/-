import sys

N = int(input())

arr1 = [0 for i in range(N)]

arr1 = list(map(int, input().split()))

# 문자열화하여 해당 character들을 int화 하여 더한다
arr2 = [0 for i in range(N)]
for i in range(len(arr1)):
    #print(list(str(arr1[i])))
    m = list(str(arr1[i]))
    for j in range(len(m)):
        arr2[i] += int(m[j])

arr_max = 0
for i in range(len(arr2)) :
    if arr_max < arr2[i] :
        arr_max = arr2[i]

index1 = arr2.index(arr_max)

print(arr1[index1])

# 몫과 나머지를 구하여 자릿수를 구할 수 있다
"""def degit_sum(x):
    sum = 0
    while x>0:
        sum+=x%10
        x=x//10
    
    return sum
"""