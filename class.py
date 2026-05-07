class User:
    def __init__(self, name, age):  # class에서 생성자는 __init__(self) 사용.
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name}")

user = User("JIN", 30)
print(user.name)
user.introduce()