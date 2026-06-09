nums = list(map(int, input().split()))
def solve():
    for A in range(1,38):

        for B in range(1,38):
            
            for C in range(1,38):

                for D in range(1,38):
                    list=[]
                    list =[A, B, C, D, A+B, B+C, C+D, D+A, A+C,B+D, A+B+C, A+B+D, A+C+D, B+C+D, A+B+C+D]
                    if sorted(list)==sorted(nums):
                        return f"{A} {B} {C} {D}"

print(solve())

    # Please write your code here.