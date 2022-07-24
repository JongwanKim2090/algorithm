n, m, k = map(int, input().split()) # n: len(list), m: count of addition, k: overlap of addtion
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1))*k
count += m % (k+1)

result_r = 0
result_r += (count) * first
result_r += (m-count) * second

print(result_r)