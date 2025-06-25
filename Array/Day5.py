'''
Reverse the Array
'''

arr = [1,2,3,4,5]

# arr.reverse()
# print(arr)

# print(arr[::-1])

s = 0
t = len(arr)-1

while t>=s:
    arr[s],arr[t] = arr[t],arr[s]
    s+=1
    t-=1

print(arr)