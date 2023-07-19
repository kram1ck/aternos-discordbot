It is a small and simple discord bot "Aternos".
It manages browser Chrome and module selenium to control the webpage.

Before the start, you need:
1) Install Chrome (version 114.0.5735.201 and higher)
2) Write into configs.txt file: 
   your AUTH_NAME and AUTH_PASSWORD (login data - login and password) Aternos account (so bot can auth on server), 
   ROLE_NAME or ROLE_ID if you need to limit using bot commands by discord role
   (if you don't need it, you should write into ROLE_NAME @everyone), 
   SERVER_NUMBER, it is a num of server in account server menu. The first server num will be 0, the second will be 1 and etc.

For example:
```
{
    "AUTH_NAME": "MYLOGIN", 
    "AUTH_PASSWORD": "MYPASSWORD",
    "ROLE_NAME": "MY SERVER ROLE",
    "ROLE_ID": 1234567,
    "SERVER_NUMBER": 0
}
```

3) Also you need a bot token. You can get it on https://discord.com/developers/applications/ by creating new bot application
   You must create a new environment variable BOT_TOKEN and write there your bot token. Don't forget to allow bot send messages in bot settings on the webpage

Enjoy!


------------------------------------------------------------------------------------------------
Это маленький и простой дискорд бот "Атернос"
Он управляет браузером Chrome и модулем selenium для контроля за страницами

Для начала, вам нужно:
1) Установить Chrome (версия 114.0.5735.201 и выше)
2) Вписать в configs.txt файл:
   ваш AUTH_NAME и AUTH_PASSWORD (данные логина и пароля) Атернос аккаунта (чтобы бот мог авторизироваться на вашем аккаунте и сервере)
   ROLE_NAME или ROLE_ID если вам нужно ограничить использование бота вашей дискорд ролью 
   (если вам это не нужно, то вам следует вписать в ROLE_NAME @everyone),
   SERVER_NUMBER, это номер сервера в меню серверов. Первый сервер будет иметь номер 0, второй будет иметь номер 1 и так далее.

Например:
```
{
    "AUTH_NAME": "MYLOGIN", 
    "AUTH_PASSWORD": "MYPASSWORD",
    "ROLE_NAME": "MY SERVER ROLE",
    "ROLE_ID": 1234567,
    "SERVER_NUMBER": 0
}
```

3) Также вам нужен бот токен. Вы можете получить его на сайте https://discord.com/developers/applications/ просто создав приложение бота
   Вам нужно создать переменную окружения BOT_TOKEN и вписать в неё ваш бот токен. Не забудьте разрешить боту отправлять сообщения в настройках бота на сайте

Наслаждайтесь
 
