'''
🧠 Problem 7 (Modified): Two Sum with Duplicates

You are given a list of integers and a target number.
Return the indices of the first pair of elements that add up to the target.
Note: The list may contain duplicate values. Return the first correct pair of indices you find (in order of appearance).

🧩 Input:

List of integers nums

Integer target

🧩 Output:

A list [i, j] where nums[i] + nums[j] == target and i < j

🔢 Example:

python
Copy
Edit
nums = [5, 5, 6, 7, 5]  
target = 10
✅ Output: [0, 1] (because 5 + 5 = 10, and this is the first valid pair)

'''

nums = [5,5,6,7,5]
list1 = []
target = 10

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            list1.append(i)
            list1.append(j)
            break
    if list1:
        break

print(list1)
