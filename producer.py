import stomp
import time

conn = stomp.Connection()
conn.start()
conn.connect('admin', 'password', wait=True)
conn.send(body='gb', destination='/queue/test')
