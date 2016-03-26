# ### 抽象
# 判断对象object的属性（name表示）是否存在
from string import Template

print(hasattr(object, 'name'))


def sample():
    """sample doc"""
    # 如上是一个_doc_,可以访问：s.__doc__
    print('test')


# 所有的函数返回None

# 复制列表要复制其副本，而不是引用


# 书上这个例子不对。。。
storage = {'first': {}, 'second': {}, 'last': {}}
# first对应的是一个键值对
me = 'He Guanyuan'
# 这样的话，键是'he'，值是[]，然后append追加才可以
storage['first']["he"] = [me]

storage['second']["guan"] = [me]
storage['last']["yuan"] = [me]
he = "He Guanxin"
storage['first']["he"].append(he)
storage['second']["guan"] = [he]
print("he__" + str(storage['first']['he']))


# 位置参数（放在前面），关键字参数（可以给定默认参数）

# 测试一下参数的收集,函数的定义和调用要对应，**有没有都可以
def with_stars(parms):
    print(parms)
    print('My name is %s , my age is %s !' % (parms['name'], parms['age']))


p = {'name': 'heguanyuan', 'age': '23'}
with_stars(p)

# 5、作用域
# 每个函数调用都会创建一个新的作用域
# 重绑定全局变量：global

# 判断是否为数字或者字母
print('12'.isalnum())
# 返回sum
print(sum([1, 2, 3, 4, 5]))
