'''
Chef was stacking plates with numbers on them. Whenever the current plate had a number less than or equal to the plate just before it, he removed both plates.

You have to simulate this and return the final stack of plates.

🧩 Input: A list of integers
🧩 Output: Final stack as a list

🔢 Example:
Input: [3, 4, 2, 2, 5]
Step-by-step:

Push 3 → [3]

Push 4 → [3, 4]

2 comes → 2 ≤ 4 → remove both → [3]

2 comes → 2 ≤ 3 → remove both → []

5 comes → [5]

✅ Final Output: [5]
'''

old = [3, 4, 2, 2, 5]
new = []

for ele in old:
    if new and ele <= new[-1]:
        new.pop()
    else:
        new.append(ele)

print(new)



