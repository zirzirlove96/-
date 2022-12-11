import sys

arr=[5,3,7,9,2,5,2,6]
arrMin = float('inf') #파이썬에서 제일 큰 값을 불러옴

#제일 큰 값을 기준으로 비교하여 제일 작은 값을 추려낸다
for i in range(len(arr)):
    if arrMin > arr[i]:
        arrMin = arr[i]

print(arrMin)