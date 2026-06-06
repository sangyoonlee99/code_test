n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)
x_min = ranges[0][1]
for x in range(1,ranges[0][1]//2+1):
    cur = x
    for i,(a,b) in enumerate(ranges):
        
        cur*=2
        if cur<a or cur>b:
            break
    else :
        x_min = min(x,x_min)

print(x_min)
    






# Please write your code here.