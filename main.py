"""General Testing in  Python"""

def hello_world():
  print("%s" % ("Hello World!"))
  print("This method prints two things!")

hello_world()

from Classes.Car import Car

first = Car("green", "Mercedez", "Benz")

print(first)

first.turn_on()

print(first)