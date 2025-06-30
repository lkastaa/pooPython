#Class Exemple
class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def presentation(self):
    return f"Hello, my name is {self.name} and i am {self.age} years old"
  
person1 = Person("Jonas", 19)
message = person1.presentation()

# or

person2 = Person(name= "JoninhasCraft", age= 19)
message2 = person2.presentation()

print(f"{message} \n{message2}")
  