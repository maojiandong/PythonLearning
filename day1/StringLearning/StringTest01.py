print('1234abcd')
print('5\'4"')
print('\"A\X34\O56')
print('\a\bc\td')
a = "123456789123"
print(a[5])
# 切片
print(a[3:7])
# 步长为2 对应位置的意思 起始:终止:步长
print(a[3::2])
# 打印到最后
print(a[1:])
# 倒着打印 第一个-1表示起始，第二个-1表示步长
print(a[-1::-1])

# 关于center的使用
print('-------------------------')
print(a.center(20,'@'))  # @@@@@123456789@@@@@@

# 关于count的使用
print(a.count('123', 4))

# 关于replace替换
print(a.replace('123', 'abc'))
