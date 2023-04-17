#Task_3
#Variant_1
def count_digits(num):
    return len(str(num))

def count_two_and_three_digit_nums(*nums):
    two_digit_count = 0
    three_digit_count = 0
    for num in nums:
        num_digits = count_digits(num)
        if num_digits == 2:
            two_digit_count += 1
        elif num_digits == 3:
            three_digit_count += 1
    print(f"Number of two-digit numbers: {two_digit_count}")
    print(f"Number of three-digit numbers: {three_digit_count}")
count_two_and_three_digit_nums(100,23,2344,234)

#Variant_2
def count(*args):
    two_digit = 0
    three_digit = 0
    for arg in args:
        digits = len(str(arg))
        print(f"Number of digits in {arg}:{digits}")
        if digits ==2:
            two_digit+=1
        elif digits ==3:
            three_digit+=1
    print(f"Number of two-digit numbers: {two_digit}")
    print(f"Number of three-digit numbers: {three_digit}")
count(234,3546,2,456,346457,345,456,23,35,65)