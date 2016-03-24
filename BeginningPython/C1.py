# print("123" + 1) 不行
# 只能用 repr(1)
print("1:" + repr(1))

# repr和str 的区别 ：str()出来的值是给人看的。。。repr()出来的值是给python看的 ?
print("2:" + repr(','))
print("3:" + str(','))

# 1.12.1
# 2**3 % 3 = 2
print("4:" + repr(pow(2, 3, 3)))

# 四舍五入,表示一位小数
print("5:" + str(round(1.19, 1)))
