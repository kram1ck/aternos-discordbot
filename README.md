# Description

It is a small project Aternos Discord bot. it released using Selenium 4

___
# Settings up

Before the start, you need:
1) Install Chrome (version 114.0.5735.201 and higher)
2) Write into configs.txt file: 
   - **Your Login and Password** into AUTH_NAME and AUTH_PASSWORD fields
   - **ROLE_NAME or ROLE_ID** if you need to limit using bot commands by discord role. If you wanna make your bot useful for everyone, you should write there `"everyone"`
   - **SERVER_NUMBER**, it is a num of server in account server menu. The first server num will be 0, the second will be 1 and etc
   - **BOT_TOKEN**, it is a token bot from website https://discord.com/developers/applications/ which you can get by creating a new bot application
   - **HEADLESS_MODE**. It is a param of silence browser. If you wanna make it visible, write into it values "False" or "".

For example:
```json
{
    "AUTH_NAME": "HelloWorld", 
    "AUTH_PASSWORD": "2432jgkd",
    "ROLE_NAME": "@everyone",
    "ROLE_ID": 1234567,
    "SERVER_NUMBER": 0,
    "BOT_TOKEN": "Mfgfkeeivmd",
    "HEADLESS_MODE": "True"
}
```

Besides configs, you can write BOT_TOKEN into environment variables. It will be written from there, too

____
# How to start bot

The only way to launch bot - from the `main.py` file in main directory of the project. If you made configs good then it will work.

___
# Bot commands

Command prefix bot is a dot `"."`
Aternos bot can handle follow commands
1) .запуск | .запусти --> Launch server
2) .закрыть | .закрой --> Stop server
3) .перезапусти | .перезагрузи --> Restart server
4) .статус --> Show current status server
5) .инфо --> Show full info about current choosen server
6) .хелп --> Show list of commands

 
