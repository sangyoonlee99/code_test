n = int(input())
B = list(map(int, input().split()))


for first in range(1,n+1):   # 첫번째 넣을 숫자 선택
    A=[0]
    A[0]=first
    ok=True

    for idx,s in enumerate(B):  # 정해진 첫번째 숫자에 맞춰서 리스트 생성
        A.append(s-A[idx])

        if A[idx+1] <= 0 or A[idx+1]>n  :
            ok=False
            break

        if len(set(A))!=len(A):
            ok=False
            break
    
    if ok:
        print(*A)
        break




    






# Please write your code here.