class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_hobby(self, hobby):
        self.hobby = hobby
        return "set hobby successfully"

    def get_hobby(self):
        print(self.hobby) #该方法的默认返回值为None


p = person("pinkman", 25)
p.set_hobby("drink alcohol")
p.get_hobby()
