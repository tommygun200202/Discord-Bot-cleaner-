Welcome to the Bot cleaner bot- the moderation bot to stop those pesky bots entering your server!

A few notes before you get started with the bot-
     
1) Before using the bot- Please create a MongoDB (atlas) for the bot.   
2) run these commands-   
```
pip install —user -r requirements.txt
python3 bot.py
```
3) Update the variables in config.py   

4) Import Names.json and Bots.json into a mongodb database called “hackathon” on the mongodb

4) Set all the settings, they MUST be set before the bot will work properly.
```
b!settings confirmedBot.action <ban|kick|none> # this setting defines what happens when a user who is a KNOWN bot joins the server
b!settings botFinder.acceptableRisk <0-3> # this setting defines how many checks a user has to pass to be ‘not a bot’. We reccomend 2. Do not use negative numbers.
b!settings botFinder.action <ban|kick|none> # this setting defines what happens when a bot fails more checks than the acceptable risk
```
Our bot is designed to save admins time by banning bots that spread inappropriate links/messages to minors and other members. We have also designed the bot using a point system. We also have included some basic moderation commands for you to use!

I hope you enjoy the bot and if you have any questions~ please message one of our developers/admins-

```
Tommyboi~#2002
Scottybbooyy#3326
Dextication#2869
```
