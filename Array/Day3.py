'''
Given a list of nums, find the majority element, the element that appears more than [n/2] times you may assume that the majority elements always exists in the array.

ex :- nums = [3,2,3]
op -> 3

ex :- nums = [2,2,1,1,1,2,2]
op -> 2

'''

list1 = [2,2,1,1,1,2,2]
n = len(list1)/2

dict1 = {}

for ele in list1:
    if ele in dict1:
        dict1[ele]+=1
    else:
        dict1[ele]=1

for k,v in dict1.items():
    if v > n:
        print(k)
        break