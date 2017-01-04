import socket
from settings import HOST, PORT, PASS, IDENT, CHANNEL


def openSocket():
	''' Open a connections to Twitch IRC using sockets '''
	bot_socket = socket.socket()
	bot_socket.connect((HOST, PORT))
	bot_socket.send("PASS " + PASS + "\r\n")
	bot_socket.send("NICK " + IDENT + "\r\n")
	bot_socket.send("JOIN #" + CHANNEL + "\r\n")
	return bot_socket


def sendMessage(bot_socket, message):
	''' Sends a Message through the socket. '''
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	bot_socket.send(messageTemp + "\r\n")
	print("SENT: " + messageTemp)
