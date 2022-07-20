''' two point problem'''
n = 5
m = 5

data = [1, 2, 3, 2, 5]

start = 0
end = 0

count = 0
sum = 0

for start in range(len(data)):
    # 스타트 하나씩  증가
    # 인접한  합이  기준값보다 큰 지  아닌지 비교
    # 맞으면  카운트 증가 하고  스타트  값  증가
    # 아니면  end increase and next array value addtion
    while sum < m and end < len(data):
        sum+=data[end]
        end+=1
    if sum == m:
        count+=1
    sum -= data[start]

print(count)
