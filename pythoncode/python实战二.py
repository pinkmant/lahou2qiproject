import yaml
class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def run(self):
        print(f"{self.name} could run")

    def bark(self):
        print(f"{self.name} could bark")


class Cat(Animal):
    def __init__(self, name, color, age, gender, hair):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = hair

    def catch_mouse(self):
        print(f"{self.name} could catch mouses")

    def bark(self):
        print(f"{self.name} could miaomiao")


class Dog(Animal):
    def __init__(self, name, color, age, gender, hair):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = hair

    def watch_house(self):
        print(f"{self.name} could watch the house")

    def bark(self):
        print(f"{self.name} could wangwang")

if __name__ == '__main__':
    with open("data.yml") as f:
        datas = yaml.safe_load(f)

cat = datas["cat"]
dog = datas["dog"]

mimi = Cat(*cat)
mimi.catch_mouse()
print(f"{mimi.name},{mimi.color},{mimi.age} age,{mimi.gender},has {mimi.hair},have catched a mouse")

tom = Dog(*dog)
tom.watch_house()
print(f"{tom.name},{tom.color},{tom.age} age,{tom.gender},has {tom.hair}")

