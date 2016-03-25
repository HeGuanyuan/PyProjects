from Tools.scripts.treesync import raw_input

# 输入用户名的例子
# 要注意 raw_input()的时候，空格也是判定非空的，要strip

name = ''
while not name:
    name = input('please enter your name:')
print('name is : ' + name.strip())

strings = "abcdefghi"
for string in strings:
    # if 'abc' in string:
    print(string)

for index, string in enumerate(strings):
    if "abc" in string:
        print(index)

for i in range(1, 100, 1):
    print('not')
    if i == 50:
        print(i)
        # 此处break会导致else执行不到
        break
else:
    print("got?")

# 列表推导式
a = [x ** 2 for x in range(10) if x % 2 == 0]
print('列表推导：' + str(a))

# pass: 空代码块是非法的，用pass占位
# del：删除不再使用的对象，删除名称，解释器会负责内存的回收
