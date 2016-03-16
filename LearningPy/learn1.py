#! /usr/bin/python //指定解释器
# Filename:helloworld.py
print("False")
print('{0: 0.3}'.format(1 / 3))
print('我是{name}'.format(name='123'))
print('{0:*^120}'.format('hello'))
print('woshi', 'hgy', 'ni', sep="")


def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


def total(initial=5, *numbers, **keywords):
    count = initial
    # total(10, 1, 2, 3, vegetables=50, fruits=100)
    # 列表 numbers = (1,2,3)
    # 字典 keywords = {'vegetables': 50, 'fruits': 100}
    print(numbers)
    print(keywords)
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


print(total(10, 1, 2, 3, vegetables=50, fruits=100))


def printMax():
    '''wode printMax'''
    return None


print(printMax.__doc__)

ab = {'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }
print("Swaroop's address is", ab['Swaroop'])

b = ['a', 'b', 'c']
a = '_'
print(a.join(b))


