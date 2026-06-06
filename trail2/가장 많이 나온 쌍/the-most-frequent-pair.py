n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

max_count = 0

for i in range(1,n+1):
    for j in range(i,n+1):  # 중복 제거   ex) (1,2)  / (2,1)
        count=0

        for a,b in pairs:
            if (a==i and b==j) or (a==j and b==i):   #모든 (i,j)에 대해서 검사
                count +=1

        max_count = max(count,max_count)

print(max_count)
# Please write your code here.