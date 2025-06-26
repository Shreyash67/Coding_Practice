'''
🧠 Problem 3: Count the Good Pairs

Arjun has a list of integers. He considers a pair (i, j) as good if:

i < j and

nums[i] == nums[j]

Your task is to count how many good pairs are there in the list.

🧩 Input: A list of integers
🧩 Output: An integer — total good pairs

🔢 Example:
Input: [1, 2, 3, 1, 1, 3]
Good pairs: (0,3), (0,4), (3,4), (2,5) → Total = 4
Output: 4
'''

nums = [1,2,3,1,1,3]

count = 0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            count+=1

print(count)