'''
🔢 Problem 6: Remove Duplicates from Sorted Array

You’re given a sorted list of integers. You need to remove the duplicates in-place, so that each element appears only once, and return the length of the new list.

Note: Don’t use extra list. Just modify the given list.

🧩 Input: A sorted list of integers
🧩 Output: Length of list after removing duplicates (list should be updated in-place)

🔢 Example:
Input: [1, 1, 2, 3, 3]
Modified List: [1, 2, 3, _, _] (ignore rest)
Output: 3
'''

n = [1, 1, 1, 2, 3]
print(len(list(set(n))))

#                                OR

# n = [1, 1, 1, 2, 3]

# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i] == n[j]:
#             n.remove(n[j])
#             n.append('_')

# count = 0
# for ele in n:
#     if isinstance(ele,int):
#         count+=1

# print(count)
