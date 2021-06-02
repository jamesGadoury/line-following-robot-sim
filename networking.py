import zmq
import json

class Publisher:
  def __init__(self, messageID, address):
    context = zmq.Context()
    self.socket = context.socket(zmq.PUB)
    self.socket.bind(address)

    self.messageID = messageID

  def publish_message(self, message):
    self.socket.send_string(f"{self.messageID}: {message}")

  def publish_message_json(self, message):
    # self.socket.send_multipart([self.messageID, json.dumps(message)])
    self.socket.send_string(self.messageID, flags=zmq.SNDMORE)
    self.socket.send_json(message)

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
      msg = self.socket.recv_string(flags=zmq.NOBLOCK)
      # return self.socket.recv_string(flags=zmq.NOBLOCK)
      print("try_get_message_string", msg)
      return msg
    except zmq.Again as e:
      # no message received yet, return empty string
      return ""
  
  def demogrify(self,topicmsg):
    """ Inverse of mogrify() """
    json0 = topicmsg.find('{')
    topic = topicmsg[0:json0].strip()
    msg = json.loads(topicmsg[json0:])
    return topic, msg 

  def try_get_message_json(self):
    try:
      # topic, message = self.demogrify(self.socket.recv(flags=zmq.NOBLOCK))
      message = self.socket.recv_multipart(flags=zmq.NOBLOCK)
      print("try_get_message_json", message)
      return json.loads(message[1])
      # print("try_get_message_string", msg)
    except zmq.Again as e:
      # no message received yet, return empty string
      return ""