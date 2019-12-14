import stomp
import time


class MyListener(stomp.ConnectionListener):

    def on_error(self, headers, message):
        print(f'received an error {message}')

    def on_message(self, headers, message):
        print(f'received a message {message}')


conn = stomp.Connection()
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)
conn.subscribe(destination='/queue/qq', id=1, ack='auto')
conn.disconnect()