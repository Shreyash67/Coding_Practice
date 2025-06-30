'''
🔁 Problem 8: Move Zeros to End

Given a list of integers, move all 0s to the end while maintaining the relative order of non-zero elements.

🧩 Input: A list of integers
🧩 Output: Modified list with 0s moved to the end (do it in-place, no new list)

🔢 Example:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
'''

l1 = [0, 1, 0, 3, 12]

for i in range(len(l1)):
    if l1[i]==0:
        l1.remove(l1[i])
        l1.append(0)

print(l1)