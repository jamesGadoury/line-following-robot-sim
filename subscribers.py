from networking import Subscriber
import json

class CommandSubscriber(Subscriber):
  def __init__(self):
    super().__init__("COMMAND", "tcp://localhost:5556")

class SensorSubscriber(Subscriber):
  def __init__(self):
    super().__init__("SENSOR", "tcp://localhost:5557")
    # self.socket.subscribe("")
    # self.socket.subscribe(self.messageID)

  def receive_readings(self):
    message = super().try_get_message_json()
    return message if message else False