from multiprocessing.connection import Client

from user import getPassword

address = ('localhost', 6000)
conn = Client(address, authkey='predator')
conn.send(getPassword('user_passwords'))
conn.send('close')
# can also send arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])
conn.close()
