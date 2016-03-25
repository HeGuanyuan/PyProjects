# # 测试1-列表的表示
# 可以这么写17*,来加入列表
from builtins import print

monthEndings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] \
               + 7 * ['th'] + ['st']
a = 1
while a < 32:
    # print("测试1：" + str(a) + monthEndings[a - 1])
    a += 1

del a

# # 测试2___通用序列操作
# 2.2.2分片
# 可以这样写tag[2:-2],print:34567;包含关系是[),左边包含，右边不包含
tag = '123456789'
# 字符串是不可改变的的对象
print("测试2:" + tag[2:-2])
# 切片的时候可以只写一边的index，比如tag[-3:],显示最后三位
print("测试2:" + tag[-3:])
# 加入步长,如下测试输出偶数
print("测试2:" + tag[1::2])
# 如果步长为负数，则取出顺序为逆向,要注意其实现方式，下例输出 321,
# 因为2是第三个，也就是‘3’，输出321，然后就是字符串尾，不包含最后一位
print("测试2:" + tag[2::-1])
# 如下的写法就是不合适的，因为从第二位反向是到不了-1位的，输出为空
print("测试2:" + tag[2:-1:-1])

# # 测试3___添加
# 初始化一个长度为10的空列表
a = [None] * 10
a = [1, 2, 3, 0]
b = [4, 5, 6]
print("测试3:a+b：" + str(a + b))
# 还有乘法
# 成员资格 1 in a,下例可以
a.append(b)
print("测试3:a.append(b):" + str(a))
print("测试3:" + str(b in a))
# 如何测试1和2都在a里面？
print("测试3:" + str([1, 2] in a))
print("测试3:" + str(min(b)))
del a
del b

# # 测试3__列表
# list("Hello") = ['H','e','l','l','o']
# 基本操作：赋值，删除
# 分片赋值_
# 一次为多个元素赋值
a = list('Panny')
a[1:] = 'ython'
# 测试3:['P', 'y', 't', 'h', 'o', 'n']
print("测试3:" + str(a))
# 插入多个元素，同理可以替换和删除
a[1:1] = '_'
print("测试3_:" + str(a))
# 列表的方法有：append,count,extend,index,insert,pop,remove,reverse,sort,sorted,
del a

# # 测试4__元组
a = 1, 32, 'wode'
print("测试4:" + str(a))
# tuple,吧序列转化为元组
# 元组的分片还是元组
# 用处：1、在映射中作为键；2、作为内建函数的方法和返回值存在
a = tuple([1, 2, 3])
print("测试4:" + str(a))
