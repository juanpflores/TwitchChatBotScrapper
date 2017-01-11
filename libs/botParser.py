#!/usr/bin/python
import json
import os
import datetime
import string

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

	chat_pivot = "#" + channel + " :"

	timestamp = str(datetime.datetime.now()).split(".")[0]
	username = getUsername(line)
	message = getMessage(line, chat_pivot)
	# mod = getMod(line)
	# sub = getSub(line)

	message_count += 1

	#We need to igonre the messages sent by other bots in the chat
	if username.endswith("bot"):
		print("[NOTIFICATION]: A Bot sent a message!")
		return
	
	print("[READ]:\t" + timestamp + "\t" + username + "\t" + message)
	print("[NOTIFICATION]: Adding message to Dictionary")
	addToDictionary(message_count, username, timestamp, message)


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


def getUsername(line):
	''' Get the username from the chat and ignores other
		bots that are in the chat. '''
	data = string.split(line, "!")
	username = data[0][1:]
	return username


def getMessage(line, pivot):
	#  We Use pivot to separate the message of the chat from
	# the text we get from the IRC. This allows us to get the
	# precise message even if the user use ":" or other simbols
	message = line.split(pivot, 1)[1]
	return message


# def getMod(line):
# 	''' Get if the user is a Mod of the channel.
# 		@authors: Safinah Ali & Joseph Seering
# 	'''
# 	separate = line.split("mod=", 1)
# 	separate2 = separate[1].split(";",1)
# 	mod = separate2[0].strip()
# 	return mod

# def getSub(line):
# 	''' Parses whether a user who sends a message is a subscriber
# 		@authors: Safinah Ali & Joseph Seering
# 	'''
# 	separate = line.split("subscriber=", 1)
# 	separate2 = separate[1].split(";",1)
# 	sub = separate2[0].strip()
# 	return sub
