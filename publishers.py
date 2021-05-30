from networking import Publisher

class CommandPublisher(Publisher):
  def __init__(self):
    super().__init__("COMMAND", "tcp://*:5556")

class SensorPublisher(Publisher):
  def __init__(self):
    super().__init__("SENSOR", "tcp://*:5557")