# -*- encoding: utf-8 -*-
# @File:   Singleton.py    
# @Time: 2020-05-22 10:03
# @Author: ZHANG
# @Description: Singleton
"""
2.
单例模式,核心结构中只包含一个被称为单例类的特殊类,类的对象只能存在一个
三个要点: 某个类只有一个实例; 必须自行创建这个实例; 必须自行向整个系统提供这个实例
"""


class Singleton1(object):
    """类变量"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton1, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance


class Myclass(Singleton1):
    a = 1


one = Myclass()
two = Myclass()

print(id(one))
print(id(two))
print(one == two)
print(one is two)

two.a = 3
print(one.a)


class Borg(object):
    """共享属性"""
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls)
        ob.__dict__ = cls._state
        return ob


class Myclass2(Borg):
    a = 1


print("=================")
one = Myclass2()
two = Myclass2()
two.a = 3
print(one.a)
print(id(one))
print(id(two))
print(one == two)
print(one is two)
print(id(one.__dict__))
print(id(two.__dict__))


def singleton(cls, *args, **kwargs):
    """装饰器"""
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class Myclass3(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


print("================")
one = Myclass3()
two = Myclass3()
two.a = 3
print(one.a)
print(id(one))
print(id(two))
print(one == two)
print(one is two)
one.x = 1
print(one.x)
print(two.x)


from target_offer.mysingleton import my_singleton
"""import 方法"""
my_singleton.foo()
