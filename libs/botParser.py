#!/usr/bin/python
import json
import os
import datetime

messages = {}
message_id = 0

def openFile(channel_name):
	start_time = str(datetime.datetime.now()).split(".")[0]
	messages['general_info'] = {
		'channel_name': channel_name,
		'start_time': start_time
	}
	general_info_json = json.dumps(messages)
	os.chdir('sample')
	print(os.getcwd())
	with open(channel_name + "-" + start_time + ".json", "w+") as sample:
		sample.write(general_info_json)


def parseChat(line, channel):

	#  We Use chat_pivot to separate the message of the chat from
	# the text we get from the IRC. This allows us to get the
	# precise message even if the user use ":" or other simbols
	chat_pivot = "#" + channel + " :"
	timestamp = str(datetime.datetime.now()).split(".")[0]

	data = string.split(line, "!")
	username = data[0][1:]

    #We need to igonre the messages sent by other bots in the chat
	if username.endswith("bot"):
		print("A Bot sent a message!")
		return

	message_id += 1
	message = line.split(chat_pivot, 1)[1]
	print("READ:\t" + timestamp + "\t" + username + "\t" + message)

openFile("juanpflores94")