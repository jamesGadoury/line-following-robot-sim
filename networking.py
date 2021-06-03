import zmq

class Publisher:
  def __init__(self, address):
    context = zmq.Context()
    self.socket = context.socket(zmq.PUB)
    self.socket.bind(address)

  def publish_message(self, message):
    self.socket.send_string(message)

  def publish_message_json(self, message):
    self.socket.send_json(message)

class Subscriber:
  def __init__(self, address):
    # set up zero mq messaging
    context = zmq.Context()
    self.socket = context.socket(zmq.SUB)

    # We subscribe to everything at this port.
    # In this design, every publisher uses a unique port
    # so we do not have to use topics.
    # I would, however, like to use topics
    # but that is an annoying rabbit hole I just jumped out of.
    # Unfortunately, if we are sending json and want it to be under a topic,
    # we need to use a multipart message.
    # Fine and dandy. However, zmq.CONFLATE does not work w/ multipart.
    # So then, we would need to roll our own process for flushing out the older messages by the subscriber.
    # Which seems more annoying than just subscribing to everything sent on this port; when each publisher has a unique port anyways.
    self.socket.subscribe("") # subscribe to everything at this port

    # Since all our subscribers care about is the most recent state, we only keep the last message received.
    self.socket.setsockopt(zmq.CONFLATE, 1)  # last msg only. 

    # Now that our socket is set up, we can connect it to the address
    self.socket.connect(address)
    

  def try_get_message_string(self):
    try:
      msg = self.socket.recv_string(flags=zmq.NOBLOCK)
      return msg
    except zmq.Again as e:
      # no message received yet, return empty string
      return ""
  
  def try_get_message_json(self):
    try:
      return self.socket.recv_json(flags=zmq.NOBLOCK)
    
    except zmq.Again as e:
      # no message received yet, return empty string
      return ""