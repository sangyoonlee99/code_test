n, m = map(int, input().split())
arr =list(map(int, input().split()))

#재귀
# def move(x,cnt):      
#     if cnt ==0:
#         return 0 

#     value = arr[x-1]
#     return value + move(value,cnt-1) 

# max_value=0

# for i in range(1,n+1):     # 시작위치 다 탐색
#     max_value = max(max_value,move(i,m))

# print(max_value)

def move(x):
    total=0
    for i in range(m):
        x=arr[x-1]
        total+=x

    return total


def bf():
    max_value=0
    for i in range(n):
        max_value=max(max_value,move(i))
    
    return max_value

print(bf())
            




# Please write your code here.