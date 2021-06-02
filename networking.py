import zmq
import json
import logging

class Publisher:
  def __init__(self, topic, address):
    context = zmq.Context()
    self.socket = context.socket(zmq.PUB)
    self.socket.bind(address)

    self.topic = topic

  def publish_message(self, message):
    self.socket.send_string(f"{self.topic}: {message}")

  def publish_message_json(self, message):
    # we need to send the topic first, so subscribers of our topic accept the message
    self.socket.send_string(self.topic, flags=zmq.SNDMORE)
    self.socket.send_json(message)

class Subscriber:
  def __init__(self, topic, address):
    # set up zero mq messaging
    context = zmq.Context()
    self.socket = context.socket(zmq.SUB)
    self.socket.connect(address)

    # only accept messages that contain topic 
    self.socket.subscribe(topic)

  def try_get_message_string(self):
    try:
      msg = self.socket.recv_string(flags=zmq.NOBLOCK)
      return msg
    except zmq.Again as e:
      # no message received yet, return empty string
      return ""
  
  def try_get_message_json(self):
    try:
      message = self.socket.recv_multipart(flags=zmq.NOBLOCK)
      return json.loads(message[1]) # index 1 is where the json is, index 0 will just be the topic we are subscribed to
    
    except zmq.Again as e:
      # no message received yet, return empty string
      return ""