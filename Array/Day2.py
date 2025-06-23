'''
Given a non-empty array of digits representing this integer by one return the updated array of digits

ex : [1,2,3] ---> 123+1 ---> 124 ---> [1,2,4]
ex : [9] ---> 9+1 ---> 10 ---> [1,0]
'''

nums = [1,2,3]
num = 0
n = 10**(len(nums)-1)

for i in range(len(nums)):
    num = num + nums[i] * n
    n = n // 10

str_num = str(num+1)

digits = []

for ele in str_num:
    digits.append(int(ele))

print(digits)