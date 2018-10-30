# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice
# in the array, and it should return false if every element is distinct.
#
# unsorted array

L1 = [4,2,8,5,9,6,5,7]

def DupicateNumber(numbers):
    if len(numbers) <= 1:
        return False
    dict_number = {}
    for i in numbers:
        if i in dict_number:
            return True
        else:
            dict_number[i] = 1

print DupicateNumber(L1)