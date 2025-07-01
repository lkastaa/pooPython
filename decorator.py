from typing import Any

# Decorator in function
def my_decorator(func):
  def wrapper():
    print("Before the function call")
    func()
    print("After")
  return wrapper

@my_decorator
def function():
  print("Function Called")

function()

# Decorator in class

class MyDecoratorInClass:
  def __init__(self, func) -> None:
    self.func = func

  def __call__(self) -> Any:
    print("Before")
    self.func()
    print("After")

@MyDecoratorInClass
def another_function():
  print("Function Called")
  
another_function()