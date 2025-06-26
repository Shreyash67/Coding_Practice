'''
🔍 Problem 5: Majority Element

Aaryan has a list of numbers. A number is called a majority element if it appears more than n/2 times, where n is the size of the list.

Your task: Find the majority element, if it exists. You can assume there's always one.

🧩 Input: A list of integers
🧩 Output: Integer — the majority element

🔢 Example:
Input: [2, 2, 1, 1, 1, 2, 2]
Output: 2 (because 2 appears 4 times, which is > 7/2 = 3.5)
'''

l1 = [2,2,1,1,1,2,2]

n = len(l1)/2

dict1 = {}

for ele in l1:
    if ele in dict1:
        dict1[ele]+=1
    else:
        dict1[ele] = 1


for k,v in dict1.items():
    if v > n:
        print(k)
        