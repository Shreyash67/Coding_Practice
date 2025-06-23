'''

Given an integer array nums, return true if any value appears at least twice in the array and return false if every element is distinct

nums = [1,2,3,1]
op ---> True

nums = [1,2,3,4]
op ---> False

'''

def my_function(list1):
    dict1 = {}

    for ele in list1: 
        if ele in dict1:
            dict1[ele]+=1
        else:
            dict1[ele]=1
    
    for key,value in dict1.items():
        if value > 1:
            return True
    else:
        return False
    
list1 = [1,2,3,4]

result = my_function(list1)

if result == True:
    print("True")
else:
    print("False")