from networking import Publisher
import json

class CommandPublisher(Publisher):
  def __init__(self):
    super().__init__("tcp://*:5556")

class SensorPublisher(Publisher):
  def __init__(self):
    super().__init__("tcp://*:5557")

  def publish_readings(self, sensorReadings):
    super().publish_message_json(sensorReadings)