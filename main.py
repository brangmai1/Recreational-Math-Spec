
"""
************ PERFECT NUMBERS ************

Definition #1:
A perfect number is a positive integer that equals the sum of its divisors except itself.

Definition #2:
A perfect number is a positive integer that is half the sum of all its divisors including itself.

Some perfect numbers: 6, 28, 496, 8128, 33550336, 8589869056, 137438691328

Unsolved perfect numbers:
1. Are there infinitely many perfect number?
2. Is there an odd perfect numbers?
"""


def is_perfect_number(test_num, method):
    divisors = []
    divisors_sum = 0

    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)

    for j in divisors:
        divisors_sum += j
    if method == 1:
        if divisors_sum == test_num:
            return True
    else:
        if clamp_test_num(divisors_sum):
            if test_num == divisors_sum / 2:
                return True
    return False


def clamp_test_num(n):
    min_lim = 0
    max_lim = 100
    if n > min_lim:
        return False
    elif n < max_lim:
        return False
    return True


print('\n********** Perfect numbers **********')
print('\nDefinition #1:')
print('A perfect number is a positive integer that equals the sum of its divisors except itself.')
print('\nDefinition #2:')
print('A perfect number is a positive integer that is half the sum of all its divisors including itself.')
print('\nChoose a solving method;')
print('\tEnter 1 to find a perfect number by using definition #1')
print('\tEnter 2 to find a perfect number by using definition #2\n')
solving_method = int(input('Your selection: '))

num = int(input('Enter a number: '))
if is_perfect_number(num, solving_method):
    print(f'{num} is a perfect number.')
else:
    print(f'{num} is not a perfect number.')
