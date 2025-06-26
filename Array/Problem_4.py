'''
🧠 Problem 4: Maximum Consecutive Ones

Kabir is working with binary data (0s and 1s). He wants to find the maximum number of consecutive 1s in the list.

🧩 Input: A list of 0s and 1s
🧩 Output: An integer — length of longest sequence of 1s

🔢 Example:
Input: [1, 1, 0, 1, 1, 1]
Output: 3 (because 1,1,1 is the longest consecutive 1s)
'''

l1 = [1,1,0,1,1,1]

count = 0 
max_count = 0

for ele in l1:
    if ele == 1:
        count += 1
        max_count = max(count,max_count)
    else:
        count = 0

print(max_count)