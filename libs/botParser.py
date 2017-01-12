#!/usr/bin/python

import json
import os
import datetime
import string
from READv3 import *

chat_log = {}
message_count = 0
file_name = ""


def createOutputFile(channel_name):
	''' Creates a Json output File on the sample folder 
	that cointains the general information about the 
	channel that includes channel name and the time 
	that the channel began being scrapped. '''
	global file_name
	start_time = str(datetime.datetime.now()).split(".")[0]
	chat_log['general_info'] = {
		'channel_name': channel_name,
		'start_time': start_time
	}
	general_info_json = json.dumps(chat_log)
	os.chdir('../sample')
	print(chat_log)
	file_name = channel_name + "_" + start_time + ".json"
	file_name.replace("\ ", "_")
	with open(file_name, "w+") as sample:
		sample.write(general_info_json)


def parseChat(line, channel):
	global message_count

	timestamp = str(datetime.datetime.now()).split(".")[0]
	username = getUser(line)
	message = getMessage(line)
	channelname = getChannelname(line)
	owner = getOwner(line)
	mod = getMod(line)
	sub = getSub(line)
	subbadge = getSubbadge(line)
	turbo = getTurbo(line)
	prime = getPrime(line)

	message_count += 1

	# We need to ignore the messages sent by other bots in the chat
	if username.endswith("bot"):
		print("[NOTIFICATION]: A Bot sent a message!")
		return
	
	print("[READ]:\t" + timestamp + "\t" + username + "\t" + message)
	# print("[NOTIFICATION]: Adding message to Dictionary")
	# addToDictionary(message_count, username, timestamp, message)


def addToDictionary(message_id, username, timestamp, message):
	'''  '''
	message_name = "message-" + str(message_id)
	chat_log[message_name] = {
		'id': message_id,
		'username': username,
		'timestamp': timestamp,
		'message': message
	}
	print("[SUCCESS]: Added message to Dictionary")
	# print(chat_log)

