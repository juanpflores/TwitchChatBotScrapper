#!/usr/bin/python
import socket
import string


class TwitchChatBotScrapper(object):

    def __init__(self, HOST, PORT, PASS, IDENT, CHANNEL):
        ''' Initialize the bot's variables. Pulling them from the
        settings.py file.'''
        self.HOST = HOST
        self.PORT = PORT
        self.PASS = PASS
        self.IDENT = IDENT
        self.CHANNEL = CHANNEL
        self.SOCKET = self.openSocket()

    def openSocket(self):
        ''' Opens a Socket conection with Twitch IRC using the
        setting the user defined in the settings.py folder.'''
        bot_socket = socket.socket()
        bot_socket.connect((self.HOST, self.PORT))
        bot_socket.send("PASS " + self.PASS + "\r\n")
        bot_socket.send("NICK " + self.IDENT + "\r\n")
        bot_socket.send("JOIN #" + self.CHANNEL + "\r\n")
        print("SOCKET opened successfully!")
        return bot_socket

    def runBot(self):
        ''' Executes the Bot. The first ste is to load the bot
        into an especific channel, once the bot is loaded sends
        message to the chat anouncing it was succesful while
        loading and starts reading the lines.'''
        readbuffer = ""
        Loading = True
        print("Joined Room")

        while Loading:
            readbuffer = readbuffer + self.SOCKET.recv(1024)
            chat = string.split(readbuffer, "\n")
            readbuffer = chat.pop()

            for line in chat:
                print(line)
                Loading = loadingComplete(line)
        self.sendMessage("Succesfully Joined Channel")
        # self.readMessages(chat_line)

    def sendMessage(self, message):
        '''Sends a Message through the socket into the channel's
        chat'''
        messageTemp = "PRIVMSG #" + self.CHANNEL + " :" + message
        self.SOCKET.send(messageTemp + "\r\n")
        print("SENT: " + messageTemp)

    def readMessages(self, chat_line):
        readbuffer = ""

        while True:
            readbuffer += self.SOCKET.recv(1024)
            chat = string.split(readbuffer, "\n")
            readbuffer = chat.pop()

            for line in chat:
                print(line)


def loadingComplete(line):
    ''' Checks if there are more messages in the chat '''
    if("End of /NAMES list" in line):
        return False
    else:
        return True
