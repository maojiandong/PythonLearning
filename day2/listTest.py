x = [1, 'mao', "xiu", 123]
print(1 in x)

# 切片赋值
L = [2, 3, 4]
# 表示0到1用后面的两个数进行替换 两个替换两个
L[0:1] = [1.1, 2.2]
M = [2, 3, 4, 5]
# 这个表示在原来0和1下标添加三个数，最后list里的元素会多出一位 三个替换两个
M[0:1] = [1.1, 2.2, 3.3]
print(L)
print(M)

N = [2, 3, 4]
# 这个表示所有的都替换 步长都是一
N[:] = [3, 4]
print(N)


# 步长为二 跳着替换
X = [1, 2, 3, 4, 5, 6]
X[0::2] = [100, 200, 300]
print(X)


# 列表推导式
y = [1, 3, 4, 5, 6]
Y = [i**2 for i in y]
print(Y)
y1 = [10, 20]
Y1 = [i*j for i in y for j in y1]  # 两层循环的嵌套
print(Y1)

# 元组
tuple1 = (20,)
tuple2 = 20,
tuple3 = 10, 20, 30
print(tuple2)
print(tuple3)

# 字典的遍历
d = {1: 100, 2: 200, 3: 300}
for k, v in d.items():
    print(k, ":", v)

# python的输入


