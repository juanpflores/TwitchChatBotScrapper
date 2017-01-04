import string
from Socket import sendMessage


def joinRoom(bot_socket):
	readbuffer = ""
	Loading = True
	print("Joined Room")

	while Loading:
		readbuffer = readbuffer + bot_socket.recv(1024)
		chat = string.split(readbuffer, "\n")
		readbuffer = chat.pop()

		for line in chat:
			print(line)
			Loading = loadingComplete(line)
			print(Loading)
	sendMessage(bot_socket, "Succesfully Joined Channel")


def loadingComplete(line):
	''' Checks if there are more messages in the chat '''
	if("End of /NAMES list" in line):
		return False
	else:
		return True
