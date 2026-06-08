n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)
def solve():
    for i in range(1,101):

        for x,y in segments :
            
            if i not in range(x,y+1):
                break
        else:
            return "Yes"
        
    else:
        return "No"
print(solve())
# Please write your code here.