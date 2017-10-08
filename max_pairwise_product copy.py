import array
a = array.array('I', xrange(10**8))
n = len(a)
import random
random.shuffle(a)


# Uses python3
#n = int(input())
#a = [int(x) for x in input().split()]
#assert(len(a) == n)


result = 0

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

max_1 = 0
#max_1_index = -1
max_2 = 0
#max_2_index = -1

# #check for max_1
# for i in range(0,n):
# 	if a[i] > max_1:
# 		max_1 = a[i]

for i in range(0,n):
	if a[i] > max_1: 
		max_1 = a[i]
		max_index = i 

a.pop(max_index)

for i in range(0,n-1):
	if a[i] > max_2:
		max_2 = a[i]


# issue when the first number if larger


# for i in range(0,n+1):
# 	if a[i] > max_1:
# 		print(i)
# 		max_2 = max_1
# 		print('max_2 is', max_2)
# 		max_1 = a[i]
# 		print('max_1 is', max_1)
# 		#max_1_index = i

# 		#max_2_index = max_1_index
# #a.pop(max_index)
# #max_2 = 0 

# for i in range(0,n-1):
# 	if a[i] > max_2:
# 		max_2 = a[i]

result = max_1 * max_2

#print(max_1)
#print(max_2)
print(result)
