# Discord-EntranceThemeBot
A Discord bot that plays intro themes and sounds for users when they join a voice channel. If a user has a sound associated with them, the bot will join the voice channel that they join, play the selected mp3/wav and leave. Intro themes are played for up to 8 seconds and then the bot will disconnect. The intro length can be adjusted on *line 32* of *MusicBot.py*.   

# How to Run in Your Discord Server:

## Notes before starting:
* You need to go to the Discord Developer Portal and create your own Discord bot following the instructions here: https://discord.com/developers/docs/intro
* After you create your bot, invite it to your server and follow the steps below
* Find your bot's token and replace the 'YOUR_TOKEN_HERE' with it in the *musicbotConfig.py* file

# 1. Download all the files from this GitHub repository
  * Make sure to put the files in a directory where you will remember
  * Run *MusicBot.py* from the directory where you stored the downloaded files in your terminal

# 2. Once the bot is running in the terminal, make sure it is online in your Discord server
  * If the bot is online, you correctly added it to your Discord server. Now you can stop running it and add your sound files:
    * Sound files must be added to the same directory as the bot files
    * Sound files must be mp3 or wav
    * Sound files must be the same name as the user that you want to associate that file with (Discord username - **DO NOT** use nickname or include user tag(#0000))
