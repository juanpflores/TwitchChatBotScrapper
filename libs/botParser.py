#!/usr/bin/python

import msgpack
import os
import datetime
import string
from READv3 import *
from colorama import init, Fore, Back, Style

chat_log = {}
message_count = 0
file_name = ""


def createOutputFile(channel_name):
	''' Creates a MSGPack output File on the sample folder
	that cointains the general information about the
	channel that includes channel name and the time
	that the channel began being scrapped. '''
	global file_name
	start_time = str(datetime.datetime.now()).split(".")[0]
	chat_log['general_info'] = {
		'channel_name': channel_name,
		'start_time': start_time
	}
	packed_data = msgpack.packb(chat_log)
	os.chdir('./sample')
	print(chat_log)
	file_name = channel_name + "_" + start_time + ".txt"
	file_name.replace("\ ", "_")
	with open(file_name, "w+") as sample:
		sample.write(packed_data)
		print(Fore.GREEN + "[SUCCESS]: Output File Created!")


def parseChat(line, channel):
	global message_count

	if "PRIVMSG" in line:
		try:
			message_name = "message-" + str(message_count)
			timestamp = str(datetime.datetime.now()).split(".")[0]
			username = getUser(line)
			message = getMessage(line)
			owner = getOwner(line)
			mod = getMod(line)
			sub = getSub(line)
			subbadge = getSubbadge(line)
			turbo = getTurbo(line)
			prime = getPrime(line)
			# print("[READ MESSAGE]:\t" + timestamp + "\t" + username + "\t" + message)
			print(Fore.YELLOW + "[NOTIFICATION]: Serializing message")
			serializeData(
				message_name, message_count, owner, subbadge, turbo, prime,
				mod, sub, username, timestamp, message)
			message_count += 1
		except Exception as e:
			print(Back.RED + Fore.WHITE + "[Error]: Message contained an error!")
			print(line)
			return

	# We need to ignore the messages sent by other bots in the chat
	# if username.endswith("bot"):
	# 	print("[NOTIFICATION]: A Bot sent a message!")
	# 	return


def serializeData(
	message_name, message_id, owner, subbadge, turbo,
	prime, mod, sub, username, timestamp, message):
	'''  '''

	# Open the target file created before. 
	with open(file_name, "r") as sample:
		data = msgpack.unpack(sample)
		# print(Fore.GREEN + "[SUCCESS]: Data Loaded from File")

	# We add the message to our dictinary of data
	data[message_name] = {
		'id': message_id,
		'owner': owner,
		'mod': mod,
		'sub': sub,
		'subbadge': subbadge,
		'turbo': turbo,
		'prime': prime,
		'username': username,
		'timestamp': timestamp,
		'message': message
	}
	print(Fore.GREEN + "[SUCCESS]: Added message " + str(message_id) + " to Dictionary")
	# print(data[message_name][message])

	# Pack data and save the file. 
	packed_data = msgpack.packb(data)
	with open(file_name, "w+") as sample:
		sample.write(packed_data)

