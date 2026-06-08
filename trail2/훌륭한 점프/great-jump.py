n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_value=100

def is_possible(x):       #x보다 작거나 같은 수들이 적혀있는 돌만 밟고 건너갈수 있다 가정,
                            # 1번 돌부터 n번 돌까지 밟을 수 있는지 판정해보자 / 그래서 가장 큰 값이 정답
    possible_box=[]

    if arr[0]>x or arr[-1]>x :   # 처음 시작, 맨끝은 x 보다 작아야지 (밟는거니까)
        return False
    for i,j in enumerate(arr):   
        if x >= j :          
            possible_box.append(i)

    for i in range(1,len(possible_box)):         
        if possible_box[i]-possible_box[i-1] > k  : #인덱스 적혀있는 리스트의 앞 뒤 차이 = 돌 사이의 거리        
            return False                         # 거리가 k 보다 크면 실패
    return True

for i in range(min(arr),max(arr)+1):
    if is_possible(i):
        min_value=min(i,min_value)

print(min_value)
        

# Please write your code here.