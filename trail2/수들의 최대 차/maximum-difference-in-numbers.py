N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

max_count=0
for i in arr:     # 범위 설정 
    count=0
    for j in arr:     #  배열 안 숫자 하나씩 탐색 
        if j in range(i,i+K+1):
            count+=1
    max_count = max(count,max_count)

print(max_count)





# Please write your code here.