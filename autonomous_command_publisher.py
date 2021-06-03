from publishers import CommandPublisher
from subscribers import SensorSubscriber
import time
import logging
import json

class AutonomousCommandPublisher(CommandPublisher):
  def __init__(self):
    super().__init__()

    self.sensorSubscriber = SensorSubscriber()
    self.sensorReadingsReceived = 0
    self.commandsPublished = 0

  def process_sensor_readings(self):
    sensorReadings = self.sensorSubscriber.receive_readings()

    if not sensorReadings:
      return

    self.sensorReadingsReceived += 1
    logging.debug(f"process_sensor_readings: {self.sensorReadingsReceived}")

    logging.info(f"Received sensor readings: {json.dumps(sensorReadings)}")
    commands = []

    if sensorReadings["center"]:
      commands.append("stop_turning")
      commands.append("move_forward")
    elif sensorReadings["left"]:
      commands.append("stop_moving")
      commands.append("turn_left")
    elif sensorReadings["right"]:
      commands.append("stop_moving")
      commands.append("turn_right")
    else:
      commands.append("stop_turning")
      commands.append("stop_moving")

    message = ",".join(commands)
    logging.info(f"Commanding: {message}")
    self.publish_message(message)

    self.commandsPublished += 1
    logging.debug(f"Sent robot commands: {self.commandsPublished}")

if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  publisher = AutonomousCommandPublisher()

  while True:
    time.sleep(0.1)
    publisher.process_sensor_readings()