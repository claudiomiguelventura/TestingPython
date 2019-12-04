class Car(object):
  def __init__(self, color, brand, model):
    from .Car import Car
    self.color = color
    self.brand = brand
    self.model = model
    self.state = "off"
  
  def __repr__(self):
    return "This car is a %s %s %s and is %s" % (self.color, self.brand, self.model, self.state)
  
  def turn_on(self):
    self.state = "on"
  
  def turn_off(self):
    self.state = "off"
