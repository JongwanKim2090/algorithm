''' two point problem'''
n = 5
m = 5

data = [1, 2, 3, 2, 5]

start = 0
end = 0

count = 0
sum = 0

for start in range(len(data)):
    while sum < m and end < len(data):
        sum+=data[end]
        end+=1
    if sum == m:
        count+=1
    sum -= data[start]

print(count)
