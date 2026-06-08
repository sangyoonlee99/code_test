a, b = map(int, input().split())
c, d = map(int, input().split())

A = list(range(a,b+1))
B = list(range(c,d+1))

if len(set(A+B)) != (len(A)+len(B)):
    print(len(set(A+B))-1)
else:
    print(len(A)+len(B)-2)

# Please write your code here.