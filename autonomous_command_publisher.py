from publishers import CommandPublisher
from subscribers import SensorSubscriber

class AutonomousCommandPublisher(CommandPublisher):
  def __init__(self):
    super().__init__()

    self.sensorSubscriber = SensorSubscriber()

  def process_sensor_readings(self):
    sensorReadings = self.sensorSubscriber.receive_readings()
    print(sensorReadings)
    if not sensorReadings:
      return
    
    if sensorReadings["left"]:
      self.publish_message("turn_right")
    elif sensorReadings["right"]:
      self.publish_message("turn_left")
    elif sensorReadings["center"]:
      self.publish_message("move_forward")
    else:
      self.publish_message("stop_turning, stop_moving")

if __name__ == "__main__":
  publisher = AutonomousCommandPublisher()

  while True:
    publisher.process_sensor_readings()