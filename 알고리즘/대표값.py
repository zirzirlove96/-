import sys
import math

N = int(input())

arr = list(map(int, input().split()))

SUM=0

for i in range(N):
    SUM += arr[i]

#평균
arrAVG = math.ceil(SUM / N)
#print(math.ceil(arrAVG))

arr2 = [] #평균과 같을 경우
arr3 = [] #평균과 다를 경우
for i in range(N):
    if arr[i] == arrAVG :
        arr2.append(i)
    else :
        arr3.append(arr[i])

#print(arr2)
#print(arr3)

arr4 = []

if len(arr2) > 0:
    print(str(arrAVG) + " " + str(arr2[0]+1))
else :
    for j in range(len(arr3)):
        if arr3[j]-arrAVG > 0 :
            arr4.append(arr3[j]-arrAVG)
        else :
            arr4.append(arrAVG - arr3[j])
    #print(arr4)
    arrFL = float('inf')
    for k in range(len(arr4)):
        if arrFL > arr4[k]:
            arrFL = arr4[k]
    #print(arrFL)
    
    arr5 = []

    for k2 in range(len(arr4)) :
        if arr4[k2] == arrFL :
            arr5.append(k2)

    #print(arr5)

    arrFL = -1
    for i in arr5:
        if arrFL < arr3[i]:            
            arrFL = arr3[i]
            print(arrFL)
    
    print(str(arrAVG) + " " + str(arr3.index(arrFL)+1))
