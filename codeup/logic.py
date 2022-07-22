a, b = map(int, input().split())
x = bool(a)
y = bool(b)

# XOR
print((x and (not y)) or ((not x) and y))

# XNOR 
print((x and y) or ((not x) and (not y)))

# NOR
print(not(x or y))

# NAND
print(not(x and y))