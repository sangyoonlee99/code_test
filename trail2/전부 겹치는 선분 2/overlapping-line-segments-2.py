n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]
def solve():
    for i in range(n):
        current_x1 = x1[:i]+x1[i+1:]
        current_x2 = x2[:i]+x2[i+1:]

        if max(current_x1) <= min(current_x2):
            return "Yes"
    return "No"

print(solve())
        
            

        











# Please write your code here.