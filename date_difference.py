'''
Snippet that displays difference (in days) between two given dates

Input:
    date1 (list): First date in format <year> <month> <day>
    date2 (list): First date in format <year> <month> <day>

Computes:
    int: The difference between given dates

Expanded form:
    print('Difference [days]: {}'.format(abs(
        (__import__('datetime').date(
            *[int(i) for i in input('<year> <month> <day>: ').split()]) -
        __import__('datetime').date(
            *[int(i) for i in input('<year> <month> <day>: ').split()])).days)))
'''
print('Difference [days]: {}'.format(abs((__import__('datetime').date(*[int(i) for i in input('<year> <month> <day>: ').split()]) - __import__('datetime').date(*[int(i) for i in input('<year> <month> <day>: ').split()])).days)))
