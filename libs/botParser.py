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
new_subs_count = 0


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
    '''Parses a message into smaller components to be serialized.'''
    global message_count
    global new_subs_count

    if "just subscribed" in line:
        try:
            message_name = "subscription-" + str(new_subs_count)
            username = getSubscriberName(line)
            prime = getTwitchPrimeSubs(line)
            timestamp = str(datetime.datetime.now()).split(".")[0]
            sub_id = new_subs_count
            print(Fore.YELLOW + "[NOTIFICATION]: Serializing Subscriber")
            serializeSubData(message_name, sub_id, username, prime, timestamp)
        except Exception as e:
            print(Back.RED + Fore.WHITE +
                  "[Error]: Message contained an error!")
            print(line)
            return

        new_subs_count += 1

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
            print(Fore.YELLOW + "[NOTIFICATION]: Serializing message")
            serializePRIVMSData(
                message_name, message_count, owner, subbadge, turbo, prime,
                mod, sub, username, timestamp, message)
            message_count += 1
        except Exception as e:
            print(Back.RED + Fore.WHITE +
                  "[Error]: Message contained an error!")
            print(line)
            return


def serializePRIVMSData(
        message_name, message_id, owner, subbadge, turbo,
        prime, mod, sub, username, timestamp, message):
    '''Opens the target file where we store all the data,
    adds the parsed data into the dictionary where we loaded
    previous data and then re-writes the file with the new
    Dictionary.'''

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
    print(Fore.GREEN + "[SUCCESS]: Added message " +
          str(message_id) + " to Dictionary")

    # Pack data and save the file.
    packed_data = msgpack.packb(data)
    with open(file_name, "w+") as sample:
        sample.write(packed_data)


def serializeSubData(message_name, sub_id, username, prime, timestamp):
    '''Serialize New subscription data'''
    # Open the target file created before.
    with open(file_name, "r") as sample:
        data = msgpack.unpack(sample)

    data[message_name] = {
        'id': sub_id,
        'username': username,
        'timestamp': timestamp,
        'prime': prime
    }

    print(Fore.GREEN + "[SUCCESS]: Added Subscription " +
          str(message_id) + " to Dictionary")

    # Pack data and save the file.
    packed_data = msgpack.packb(data)
    with open(file_name, "w+") as sample:
        sample.write(packed_data)
