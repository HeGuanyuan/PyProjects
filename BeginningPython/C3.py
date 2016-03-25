from string import Template
import string

# # 1、标准的序列操作对字符串都适用

# # 2、格式化，简版。注意此处只能使用元组
f = "Hello,%s,%s!"
v = 'heguanyuan', 'my load'
print(f % v)
# 另一种：模板字符串
s = Template('My name is $name!')
print(s.substitute(name='guanyuan'))
# 如果是单词的一部分
st = Template('My name is he${name}')
print(st.substitute(name='guanyuan'))
# 避免少值，用safe_substitute
# 字符串常量
print(string.printable)

# 注意join方法，连接序列中的元素，而split是将字符串分割为序列
l = list('heguanyuan')
sep = '_'
print('join_:' + sep.join(l))
# strip是去除两侧的空格
# translate替换单个字符，可同时替换多个位置

table = str.maketrans('cs', 'kz')
print('table.len: ' + str(len(table)))
# 一下输出：table: {115: 122, 99: 107}
print('table: ' + str(table))
# translate cs -> kz
print("cs.trans: " + 'cs'.translate(table))
