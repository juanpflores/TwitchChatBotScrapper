#!/usr/bin/python

import socket
import string
import time
import datetime
from botParser import parseChat, createOutputFile
from colorama import init, Fore, Back, Style

# Initialize Colorama for term notifications
init(autoreset=True)


class TwitchChatBotScrapper(object):

    def __init__(self, HOST, PORT, PASS, IDENT, CHANNEL):
        ''' Initialize the bot's variables. Pulling them from the
        settings.py file.'''
        self.HOST = HOST
        self.PORT = PORT
        self.__PASS = PASS
        self.IDENT = IDENT
        self.CHANNEL = CHANNEL
        self.SOCKET = self.openSocket()

    def openSocket(self):
        ''' Opens a Socket conection with Twitch IRC using the
        setting the user defined in the settings.py folder.'''
        bot_socket = socket.socket()
        bot_socket.connect((self.HOST, self.PORT))
        bot_socket.send("PASS " + self.__PASS + "\r\n")
        bot_socket.send("CAP REQ :twitch.tv/commands" + "\r\n")
        bot_socket.send("CAP REQ :twitch.tv/tags" + "\r\n")
        bot_socket.send("NICK " + self.IDENT + "\r\n")
        bot_socket.send("JOIN #" + self.CHANNEL + "\r\n")
        print(Fore.GREEN + "[SUCCESS]: SOCKET opened!")
        return bot_socket

    def closeSocket(self):
        self.SOCKET.send("QUIT\r\n")

    def loadBot(self):
        ''' Executes the Bot. The first ste is to load the bot
        into an especific channel, once the bot is loaded sends
        message to the chat anouncing it was succesful while
        loading and starts reading the lines.'''
        readbuffer = ""
        Loading = True
        print("Joined Room")
        print(Back.YELLOW + Fore.WHITE + "[NOTIFICATION]: Loading..")

        while Loading:
            readbuffer = readbuffer + self.SOCKET.recv(1024)
            chat = string.split(readbuffer, "\n")
            readbuffer = chat.pop()

            for line in chat:
                # print(line)
                Loading = loadingComplete(line)
                if Loading == False:
                    break
        # self.sendMessage("Hola a Todos!")

    def sendMessage(self, message):
        '''Sends a Message through the socket into the channel's
        chat'''
        messageTemp = "PRIVMSG #" + self.CHANNEL + " :" + message
        self.SOCKET.send(messageTemp + "\r\n")
        print("SENT: " + messageTemp)

    def readMessages(self):
        start_time = time.time()
        readbuffer = ""
        createOutputFile(self.CHANNEL)

        while True:
            readbuffer += self.SOCKET.recv(1024)
            chat = string.split(readbuffer, "\n")
            readbuffer = chat.pop()

            for line in chat:
                if "PING" in line:
                    self.SOCKET.send(line.replace('PING', 'PONG'))
                    print(Back.YELLOW + "[READ PING]: Responded Pong")
                else:
                    parseChat(line, self.CHANNEL)

            if time.time() > start_time + 60 * 4:
                self.closeSocket()
                self.openSocket()
                # self.loadBot()
                print(Back.YELLOW + "[NOTIFICATION]: Restarting Bot")
                start_time = time.time()


def loadingComplete(line):
    ''' Checks if the bot has completed the loading fase and returns
    a boolean to the run function.'''

    # When the bot read a /NAMES it means it has succesfully loaded
    # the target channel.
    if("End of /NAMES list" in line):
        print(Back.GREEN + Fore.WHITE + "[SUCCESS]: Loading Complete")
        return False
    else:
        return True
