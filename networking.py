import zmq

class Publisher:
  def __init__(self, messageID, address):
    context = zmq.Context()
    self.socket = context.socket(zmq.PUB)
    self.socket.bind(address)

    self.messageID = messageID

  def publish_message(self, message):
    self.socket.send_string(f"{self.messageID}: {message}")

class Subscriber:
  def __init__(self, messageID, address):
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