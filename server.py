import logging
from time import sleep
from zeroless import (Server, log)
import  paho.mqtt as mqtt

# Setup console logging
consoleHandler = logging.StreamHandler()
log.setLevel(logging.DEBUG)
log.addHandler(consoleHandler)

# Binds the publisher server to port 12345
# And assigns a callable to publish messages with the topic 'sh'
pub = Server(port=12345).pub(topic=b'sh', embed_topic=True)

# Gives publisher some time to get initial subscriptions
while True:
    sleep(1)
    for msg in [b"Msg1", b"Msg2", b"Msg3"]:
        pub(msg)