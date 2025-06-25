'''
👦 Problem 1: The Lost Number

Rahul found an old notebook in his cupboard. Inside it, there was a list of n-1 distinct numbers from 1 to n. One number is missing from the list. Rahul wants your help to find that missing number.

🧩 Input: An array of size n-1, containing integers from 1 to n with one missing.
🧩 Output: The missing number.

🔢 Example:
Input: [1, 2, 4, 5, 6]
Output: 3
'''

# Approach :- Total - sum

l1 = [1,2,4,5,6]

n = len(l1) + 1
total = n*(n+1)//2
sum_of_number = sum(l1)

missing_number = total - sum_of_number
print(missing_number)