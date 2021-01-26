# -*- coding: utf-8 -*-
# @Time   : 2021/1/26 11:01
# @Author : guoccf
# @File   : cat1.py

"""
《作业》
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】

《返回结果》
short_hair
Mimi
white
1
woman
Mimi can catch mice
Mimi can run
Mimi can meow
"""

from Two_homework.Animal import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.hair = "short_hair"

    def catching_mice(self):
        print(f"{self.name} can catch mice")

    def cry(self):
        print(f"{self.name} can meow")


if __name__ == '__main__':

    # 实例化
    cat = Cat()

    # 新属性
    print(cat.hair)

    # 继承父类的属性
    print(cat.name)
    print(cat.color)
    print(cat.age)
    print(cat.sex)

    # 新方法
    cat.catching_mice()

    # 继承父类方法
    cat.run()

    # 重写父类方法
    cat.cry()
