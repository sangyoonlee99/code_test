x1, x2, x3, x4 = map(int, input().split())

line=list(range(x3,x4+1))
for i in range(x1,x2+1):
    if i in line :
        print("intersecting")
        break
else:
    print("nonintersecting")
# Please write your code here.