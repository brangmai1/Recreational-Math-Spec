
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


def is_perfect_number(divisor_sum, test_num, method):
    if method == 1:
        if divisor_sum == test_num:
            return True
    else:
        divisor_sum += test_num
        if test_num == divisor_sum / 2:
            return True
    return False


print('\n********** Perfect numbers **********')
print('\nDefinition #1:')
print('A perfect number is a positive integer that equals the sum of its divisors except itself.')
print('\nDefinition #2:')
print('A perfect number is a positive integer that is half the sum of all its divisors including itself.')
print('\nChoose a solving method;')
print('\tEnter 1 to find a perfect number by using definition #1')
print('\tEnter 2 to find a perfect number by using definition #2\n')
solving_method = int(input('Your selection: '))

# while solving_method != range(1, 3):
#     print('Invalid solving method')
#     solving_method = int(input('Enter digit 1 or 2: '))
#     if solving_method == range(1, 3):
#         break

num = int(input('Enter a number: '))
divisors = []
added_divisors = 0

for i in range(1, num):
    if num % i == 0:
        divisors.append(i)

for j in divisors:
    added_divisors += j

if is_perfect_number(added_divisors, num, solving_method):
    print(f'{num} is a perfect number.')
else:
    print(f'{num} is not a perfect number.')
