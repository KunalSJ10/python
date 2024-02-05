def evennum(numbers):
    result = []
    for num in numbers:
        if num %2 == 0:
            result.append(num)
    return result
numbers=[1,2,3,4,5,6,7,8,9,10]
x=evennum(numbers)
print("the numbers are ",x)