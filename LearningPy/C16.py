# make_repeater 函数在运行时创建新的函数对象
def make_repeater(n):
    return lambda s: s * n

twice = make_repeater(2)
print(twice('word'))
print(twice(5))
