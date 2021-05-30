from networking import Subscriber

class CommandSubscriber(Subscriber):
  def __init__(self):
    super().__init__("COMMAND", "tcp://localhost:5556")

class SensorSubscriber(Subscriber):
  def __init__(self):
    super().__init__("SENSOR", "tcp://localhost:5557")