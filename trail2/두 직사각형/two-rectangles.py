x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

rec1_x = list(range(x1,x2+1))
rec1_y = list(range(y1,y2+1))

rec2_x = list(range(a1,a2+1))
rec2_y = list(range(b1,b2+1))


def judge():
    for x_1 in rec1_x:
        if x_1 in rec2_x :
            
            for y_1 in rec1_y:
                if y_1 in rec2_y:
                    return "overlapping"
                
    else :
        return "nonoverlapping"

print(judge())

# Please write your code here.