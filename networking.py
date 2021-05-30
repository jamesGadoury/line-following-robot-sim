import zmq

PUBLISHER_ADDRESS = "tcp://*:5556"
SUBSCRIBER_ADDRESS = "tcp://localhost:5556"

class Publisher:
  def __init__(self, messageID, address=PUBLISHER_ADDRESS):
    context = zmq.Context()
    self.socket = context.socket(zmq.PUB)
    self.socket.bind(address)

    self.messageID = messageID

  def send_message(self, message):
    self.socket.send_string(f"{self.messageID}: {message}")

class Subscriber:
  def __init__(self, messageID, address=SUBSCRIBER_ADDRESS):
    # set up zero mq messaging
    context = zmq.Context()
    self.socket = context.socket(zmq.SUB)
    self.socket.connect(address)

    # only accept messages that contain messageID 
    self.socket.setsockopt_string(zmq.SUBSCRIBE, messageID)

  def try_get_message_string(self):
    try:
      return self.socket.recv_string(flags=zmq.NOBLOCK)
    except zmq.Again as e:
      # no message received yet, return empty string
      return ""