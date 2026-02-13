from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Taro", 20)

print(p)
print(p.name)
print(p.age)