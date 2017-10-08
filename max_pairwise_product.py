# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)


result = 0

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

maximum = 0

for i in range(0,n):
	if a[i] > maximum:
		maximum = a[i]
		max_index = i
a.pop(max_index)
max_2 = 0 

for i in range(0,n-1):
	if a[i] > max_2:
		max_2 = a[i]

result = maximum * max_2


print(result)
