n = int(input())
sum = 0
while n >=1:
    if n%2==0:
        sum += n
    else:
        sum += 2*((n-1)//2)
    n = n-2

print(sum)

a = int(input())
s = 0

for i in range(1, a+1):
    if i%2 == 0:
        s += i
print(s)

b = int(input())
ss = 0
sum_while = 0 

while ss <= b:
    if ss %2 == 0:
        sum_while += ss
    ss += 1
print(sum_while)

