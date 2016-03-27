# ## 更加抽象--对象
# 这个很基础，没什么可说的；

# ##C8
# 一个输入的demo
while True:
    try:
        x = int(input("int1:"))
        y = int(input('int2:'))
        a = int(x / y)
    except Exception:
        # raise
        print('Error，invalid input')
    else:
        print('x/y=' + str(a))
        break
    finally:
        print('good luck\n')
