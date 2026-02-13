from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    # メソッドを追加
    def greet(self):
        return f"Hello, I'm {self.name}"

    def is_adult(self):
        return self.age >= 18


p = Person("Taro", 20)

print(p)
print(p.name)
print(p.age)

print(p.greet())
print(p.is_adult())