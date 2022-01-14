#数据结构类型
序列类型简介
列表 list
元组 tuple
字典 dict
集合 set


一、列表
空列表的定义
L=[]
L=list()

列表的in/not in运算符  (与string字符串一样)
x=[1,'two',3.0,"four"]
1 in x      #True
2 not in x  #True

正向索引与反向索引(等同字符串)
正向索引:0~len(x)-1
反向索引:-len(x)~-1

list的属性方法
1、list.index(v[,begin[,end]])   v查找的元素，begin从哪里开始查找，end结束索引
2、list.count(x)     返回列表中元素的个数
3、list.append(x)    在列表尾部添加单个元素
4、list.extend(list1) 向列表追加另一个列表
5、list.sort(reverse=True)  reverse=True降序，默认是升序
6、list.reverse()     反转
7、list.pop(index)    删除索引对应的元素

浅拷贝与深拷贝
list.copy()与切片复制L[:]是浅拷贝
比如L=[2,3,4]
L1=[10,L,20]
L2=L1.copy()
这里L2只是复制了表面的一层L1，把L的地址也复制进来了，如果在C++中释放，释放L1时，发现L是个指针会进行一次释放，释放L2时，发现L是个指针又会进行释放，这样L就释放了两次，会出错
深拷贝 deepcopy将对象逐层进行复制需要导包 import copy

del 运算符用于删除列表元素
del cities[2]  #删除列表中的[2]元素
del cities[0:2] #删除[0],[1]元素

列表式可迭代对象
L=[2,3,4,5]
for x in L:
    print(x)
列表推导式
语法：
[表达式 for 变量 in 可迭代对象]

---------------------------------------------------
元组tuple  相当于不可以改变的list 只不过它是括号
创建空元组
t=()
t=tuple()
非空元组
t=(20,) 含有一个元素的元组
t=20,  注意这个逗号不然就成普通变量赋值了
t=(100,200,300)
t=100,200,300

---------------------------------------------------
字典
以键值对的形式进行存储
字典的表示是以{}括起来，以冒号分割键值对，各键值对之间用逗号分隔开
字典的键不能重复   就像hashmap一样
空字典创建的方法
d={}
d=dict{}
非空
d={"name":"Tom","age":12}

不能充当键key的类型有
列表，字典，集合set
字典的遍历
d={1:100, 2:200, 3:300}
for k,v in d.items():
    print(k, ":", v)

