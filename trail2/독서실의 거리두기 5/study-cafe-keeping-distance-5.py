N = int(input())
seat = list(input())

def solve(arr):
    loc=[]
    min_value=20
    for idx,i in enumerate(arr):
        if i=="1":
            loc.append(idx)
    for i,j in zip(loc,loc[1:]):
        min_value = min(j-i,min_value)

    return min_value

def put(arr):
    max_value=0
    for idx,i in enumerate(arr):
        if arr[idx]=="0":
            arr[idx]="1"
        
            value = solve(arr)
            max_value = max(max_value,value)
            arr[idx]='0'
    return max_value
    


print(put(seat))

