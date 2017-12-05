'''
Snippet that counts number elements itterable

Args:
    itterable
'''

counter = lambda x: dict(__import__('collections').Counter(x))
