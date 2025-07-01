# Inheritance Example
class Animal:
  def __init__(self, name) -> None:
    self.name = name

  def walk(self):
    print(f"Animal {self.name} walked")
    return
  
  def make_sound(self):
    pass  
  
class Wolf(Animal):
  def make_sound(self):
    return "auuuu"
  
class Cat(Animal):
  def make_sound(self):
    return "miau!"
  
wolf = Wolf(name="Lobinhuu")
cat = Cat(name="Tom")

# Polymorphism example
animals = [wolf, cat]

for animal in animals:
  print(f"{animal.name} make {animal.make_sound()}")

# Encapsulation example
class BankAccount:
  def __init__(self, balance) -> None:
    self.__balance = balance   #Private atribute __

  def deposit(self, value):
    if value > 0:
      self.__balance += value
  
  def withdraw(self, value):
    self.__balance -= value

  def check_balance(self):
    return self.__balance
  
jonas_account = BankAccount(balance=1300)

print(f"Balance before withdraw")
print(f"Bank account balance: {jonas_account.check_balance()}")
jonas_account.withdraw(500)
print(f"Balance after: {jonas_account.check_balance()}")

# Abstraction example
from abc import ABC, abstractmethod

class Vehicle(ABC):

  @abstractmethod
  def start(self):
    pass

  @abstractmethod
  def turn_off(self):
    pass

class Car(Vehicle):
  def __init__(self) -> None:
    pass

  def start(self):
    return "Started car"
  
  def turn_off(self):
    return "Car turned off"
  
jonas_car = Car()
print(jonas_car.start())
print(jonas_car.turn_off())