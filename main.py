#!/usr/bin/python

from libs.TwitchChatBotScrapper import TwitchChatBotScrapper
from settings import HOST, PORT, PASS, IDENT, CHANNEL

chatBot = TwitchChatBotScrapper(HOST, PORT, PASS, IDENT, CHANNEL)
chatBot.openSocket()
chatBot.runBot()
