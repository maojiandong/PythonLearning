def __hello__():
    print("hello world!")

    __hello__()


# 定义函数要空两行
def __add__(a, b):
    return a+b


a1 = __add__('1', "m")
print("1+m=", a1)


# 命名关键字形参   这里表示c命名为关键字形参
def myfun1(a, b, *, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)


# 调用myfun1
# myfun1(1, 2, 3) # TypeError: myfun1() takes 2 positional arguments but 3 were given
# 正确调用方法
myfun1(1, 2, c=3)


# 函数式编程
def f():
    print("hello world!")


f1 = f
f1()
f2 = myfun1
f2(c=20, a=1, b=20)


# 函数作为返回值
def getfn():
    def print_hello():
        print("hello")
    return print_hello()


getfn()


# 函数作为函数的参数传递
def tab(x,y):
    return "|" + x.center(13) + \
    "|"+y.center(13)+"|"


def string(x, y):
    return "姓名:" + x + "年龄：" + y


def myprint(fx, x, y):
    s = fx(x, y)
    print(s)


# 第一个参数是函数，x，y对应函数的参数
myprint(tab, "Midu", "15")
myprint(string, "张三", "18")
