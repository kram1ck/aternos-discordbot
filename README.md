It is a small and simple discord bot "Aternos".
It manages browser Chrome and module selenium to control the webpage.

Before the start, you need:
1) Install Chrome (version 114.0.5735.201 and higher)
2) Write into configs.txt file: 
   your AUTH_NAME and AUTH_PASSWORD (login data - login and password) Aternos account (so bot can auth on server); 
   ROLE_NAME or ROLE_ID if you need to limit using bot commands by discord role
   (if you don't need it, you should write into ROLE_NAME @everyone); 
   SERVER_NUMBER, it is a num of server in account server menu. The first server num will be 0, the second will be 1 and etc;
   BOT_TOKEN, it is a token bot from website https://discord.com/developers/applications/ which you can get by creating a new bot application;
   HEADLESS_MODE, it is a param of silence browser. If you wanna make it visible, write into it values "False" or "".

For example:
```
{
    "AUTH_NAME": "MYLOGIN", 
    "AUTH_PASSWORD": "MYPASSWORD",
    "ROLE_NAME": "MY SERVER ROLE",
    "ROLE_ID": 1234567,
    "SERVER_NUMBER": 0,
    "BOT_TOKEN": "MY_BOT_TOKEN",
    "HEADLESS_MODE": "True"
}
```

Besides configs, you can write BOT_TOKEN into environment variables. It will be written from there, too

Enjoy!

------------------------------------------------------------------------------------------------

Это маленький и простой дискорд бот "Атернос"
Он управляет браузером Chrome и модулем selenium для контроля за страницами

Для начала, вам нужно:
1) Установить Chrome (версия 114.0.5735.201 и выше)
2) Вписать в configs.txt файл:
   ваш AUTH_NAME и AUTH_PASSWORD (данные логина и пароля) Атернос аккаунта (чтобы бот мог авторизироваться на вашем аккаунте и сервере);
   ROLE_NAME или ROLE_ID если вам нужно ограничить использование бота вашей дискорд ролью 
   (если вам это не нужно, то вам следует вписать в ROLE_NAME @everyone);
   SERVER_NUMBER, это номер сервера в меню серверов. Первый сервер будет иметь номер 0, второй будет иметь номер 1 и так далее,
   BOT_TOKEN, это токен приложения бота с сайта https://discord.com/developers/applications/ который вы можете получить, создав новое приложение-бота
   HEADLESS_MODE, это параметр скрытности браузера. Если вы хотите сделать его видимым, впишите здесь значения "False" или "".

Например:
```
{
    "AUTH_NAME": "МОЙ ЛОГИН", 
    "AUTH_PASSWORD": "МОЙ ПАРОЛЬ",
    "ROLE_NAME": "ИМЯ МОЕЙ РОЛИ",
    "ROLE_ID": 1234567,
    "SERVER_NUMBER": 0,
    "BOT_TOKEN": "МОЙ_БОТ_ТОКЕН"
    "HEADLESS_MODE": "True"
}
```

Помимо конфига, вы можете вписать BOT_TOKEN в переменные окружения. Он также будет читать оттуда.

Наслаждайтесь!
 
