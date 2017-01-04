from Socket import openSocket
from initialize import joinRoom

s = openSocket()
joinRoom(s)

while True:
	persist = True
