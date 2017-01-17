# :space_invader: TwitchChatBotScrapper :space_invader:
TwitchChatBotScrapper is a Twitch bot that uses Twitch IRC to connected to a user specified channel and saves all the messages on a MessagePack encoded file. This repo aims to help other researchers to pull data from Twitch channels  without the task of building their own chatbots or scrappers.

## Requirements
The repo uses [MessagePack](http://msgpack.org/) to serialize and store data as a Python dictionary. This helps us to save large amount of data in a fast and small way.

1. PIP
2. `pip install msgpack-python`
3. `pip install colorama`


## Installation
1. Clone or Download the Repo using this address: `https://github.com/juanpflores/TwitchChatBotScrapper.git`.
2. Get your Twitch API KEY from http://twitchapps.com.
3. Change the settings.py file with your information.
4. You'll need to install the next 

## Usage
Just run the main.py file or you can use the bot on your own projects  :thumbsup:

### On you own project
If you want to use the bot in your own project you will ned to copy the TwitchChatBotScrapper.py file and exectute `.openSocket()` then `.loadBot` and finally `.readMessage()` to allow the bot to work.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request by filling the especified information on the request.

## History
This project was develop to recolect data for ___insertPaperNameHere___ with the help of West Virginia University, Carnegie Melon Human Computer Interaction Institute and Mexico's National Autonomous University.

## Credits


## License
TODO: Write license