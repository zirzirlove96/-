import sys

n,m = map(int, input().split())
arr1=[]

for i in range(1, n+1):
    for j in range(1, m+1):
        arr1.append(i+j)

arr2=[0 for i in range(n*m)]

#값이 해당하는 인덱스에 count
for i in range(len(arr1)):
    j=1
    arr2[arr1[i]] += j 
    #print(arr2)

max_arr = 0

#카운트가 많이 올라간 값 구하기
for j in range(len(arr2)):
    if max_arr < arr2[j]:
        max_arr = arr2[j]

#위에서 구한 제일 큰 카운트에 해당하는 index 구하기
arr3 = []
for k in range(len(arr2)):
    if max_arr == arr2[k]:
        arr3.append(k)

print(arr3)
