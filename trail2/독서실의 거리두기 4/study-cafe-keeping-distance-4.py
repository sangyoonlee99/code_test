# n = int(input())
# seat = list(input())


# def solve():
#     m=n
#     min_list=[]
#     for i in range(n-1):
#         for j in range(i,n):
#             if seat[i]=="0" or seat[j]=="0":
#                 continue

#             if seat[i]=="0" and seat[j]=="0":
#                 seat[i]="1"
#                 seat[j]="1"

#             for idx,value in enumerate(seat):
#                 if value=="1":
#                     seated=[]
#                     seated.append(idx)
#             for i in range(1,len(seated)):
#                 m=seated[i]-seated[i-1]
#                 min_m = min(m,min_m)
#                 min_list.append(min_m)

#     return max(min_list)

# print(solve())
    



n = int(input())
seat = list(input())

m=100

min_list=[]


for i in range(n-1):
    for j in range(i+1,n):         # 빈자리 채우기중 하나의 경우의 수를 다 반복
        if seat[i]=="1" or seat[j]=="1":
            continue

        if seat[i]=="0" and seat[j]=="0":      # 사람없으면 사람 채우기
            temp = seat[:]
            temp[i]="1"
            temp[j]="1"
        seated=[]
        for idx,value in enumerate(temp):    # 사람있는 자리 리스트 만들기
            if value=="1":
                seated.append(idx)

        min_m=100
        for k in range(1,len(seated)):        # 사람있는 자리끼리 거리 구하기
            m=seated[k]-seated[k-1]
            min_m = min(m,min_m)            # 거리의 최소값 구하기
        min_list.append(min_m)

print(max(min_list))




            
            
            


# # Please write your code here.