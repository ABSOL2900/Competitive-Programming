import math
n, m, a=map(int, input().split())

left=math.ceil(n/a)
top=math.ceil(m/a)
a=top*left

print(a)