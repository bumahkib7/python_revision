class Car:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def drive(self):
    print("Driving", self.name)

  def stop(self):
    print("Stopping", self.name)

  def paint(self, color):
    self.color = color
    print("Painting", self.name, "with", color)
