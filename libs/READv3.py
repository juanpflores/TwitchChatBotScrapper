#!/usr/bin/python


def getUser(line):
    '''Parses the username.'''
    separate = line.split("!", 1)
    user = separate[1].split("@", 1)[0]
    return user


def getMessage(line):
    '''Parses the message of a chat line.'''
    separate = line.split("!", 1)
    message = separate[1].split(":", 1)[1]
    return message


def getChannelname(line):
    '''Parses the name of a channel.'''
    separate = line.split("!", 1)
    separate2 = separate[1].split(":", 1)
    channelnametemp = separate2[0].split("#", 1)[1]
    channelname = channelnametemp.strip()
    return channelname


def getMod(line):
    '''Parses whether a user who sends a message is a mod.'''
    separate = line.split("mod=", 1)
    separate2 = separate[1].split(";", 1)
    mod = separate2[0].strip()
    return mod


def getSub(line):
    '''Parses whether a user who sends a message is a subscriber.'''
    separate = line.split("subscriber=", 1)
    separate2 = separate[1].split(";", 1)
    sub = separate2[0].strip()
    return sub


def getSubbadge(line):
    '''Parses whether a user who sends a message has a subscriber
            badge.'''
    if "subscriber/" in line:
        separate = line.split("subscriber/", 1)
        separate2 = separate[1].split(",", 1)
        subbadge = separate2[0].strip()
        if "color=" in subbadge:
            separate = subbadge.split(";", 1)
            subbadge = separate[0].strip()
    else:
        subbadge = 0
    return subbadge


def getTurbo(line):
    '''Parses whether a user who sends a message has turbo.'''
    separate = line.split("turbo=", 1)
    separate2 = separate[1].split(";", 1)
    turbo = separate2[0].strip()
    return turbo


def getPrime(line):
    '''Parses whether a user who sends a message has prime.'''
    if "premium/" in line:
        separate = line.split("premium/", 1)
        separate2 = separate[1].split(";", 1)
        premium = separate2[0].strip()
    else:
        premium = 0
    return premium


def getOwner(line):
    '''Parses whether a user who sends a message is the channel owner'''
    mod = 1
    separate = line.split("room-id=", 1)
    separate2 = separate[1].split(";", 1)
    roomid = separate2[0].strip()
    separate = line.split("user-id=", 1)
    separate2 = separate[1].split(";", 1)
    userid = separate2[0].strip()
    if userid == roomid:
        owner = 1
    else:
        owner = 0
    return owner


def getBannedChannelname(line):
    '''Parses the name of a channel contained in a ban indicator message.'''
    separate = line.split(":", 2)
    channelnametemp = separate[1].split("#", 1)[1]
    channelname = channelnametemp.strip()
    return channelname


def getBannedUser(line):
    '''Parses the name of a user who got banned from a ban indicator.'''
    separate = line.split(":", 2)
    user = separate[2].strip()
    return user


def getBanduration(line):
    '''Parses the duration of the ban.'''
    separate = line.split("@ban-duration=", 1)
    separate2 = separate[1].split(";", 1)
    banduration = separate2[0].strip()
    return banduration


def getr9k(line):
    '''Parses mode changes in r9k'''
    separate = line.split("r9k=", 1)
    separate2 = separate[1].split(":", 1)
    if "@broadcaster-lang" in line:
        separate2 = separate2[0].split(";", 1)
    r9kmode = separate2[0].strip()
    return r9kmode


def getsubmode(line):
    '''Parses mode changes in submode.'''
    separate = line.split("subs-only=", 1)
    separate2 = separate[1].split(":", 1)
    submode = separate2[0].strip()
    return submode


def getslowmode(line):
    '''Parses mode changes in slowmode.'''
    separate = line.split("slow=", 1)
    separate2 = separate[1].split(":", 1)
    if "@broadcaster-lang" in line:
        separate2 = separate2[0].split(";", 1)
    slowmode = separate2[0].strip()
    return slowmode


def getroomstatechannelname(line):
    '''parses room state'''
    channelname = line.split("#", 1)[1]
    channelname = channelname.strip()
    return channelname
