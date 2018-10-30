# Given an array of integers that is already sorted in ascending order, find two numbers such that the add upto a specific target numbers
#
# Example : [3,5,8,10,15,21]
# Sum: 23
# Number: 8 + 15

numbers = [3,5,8,10,15,21]
sum = 15

class sumOf2Numbers(object):

    def sumOf2(self, numberList, sum):
        if len(numberList) == 0:
            return [-1]
        start = 0
        end = len(numberList) - 1
        while start < end:
            sumOfTwo = numberList[start] + numberList[end]
            if sumOfTwo == sum:
                return [start, end]
            elif sumOfTwo > sum:
                end = end - 1
            elif sumOfTwo < sum:
                start = start + 1
        return [-1]

obj = sumOf2Numbers()
index = obj.sumOf2(numbers, sum)
print(numbers[index[0]], numbers[index[1]])