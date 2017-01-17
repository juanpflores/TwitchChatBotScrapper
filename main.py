#!/usr/bin/python

from colorama import init,Fore, Back, Style
from libs.TwitchChatBotScrapper import TwitchChatBotScrapper
from settings import HOST, PORT, PASS, IDENT, CHANNEL

chatBot = TwitchChatBotScrapper(HOST, PORT, PASS, IDENT, CHANNEL)

# Initialize Colorama for term notifications
init(autoreset=True)
alive = True

while alive:
	chatBot.openSocket()
	chatBot.loadBot()
	chatBot.readMessages()
	print(Back.YELLOW + "[NOTIFICATION]: Restarting Bot")
