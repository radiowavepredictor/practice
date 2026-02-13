from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def greet(self):
        return f"Hello, I'm {self.name}"


# Person を引数に取る関数
def introduce(person: Person):
    print(f"{person.name} is {person.age} years old.")


p = Person("Taro", 20)

introduce(20)