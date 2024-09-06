#!/bin/sh

FILE=../src/.env

function setup_env(){
echo "Устанавливаются переменные окружения"

echo DEBUG="True" >> $FILE
echo ALLOWED_HOSTS="*" >> $FILE
echo CORS_ALLOWED_ORIGINS="http://127.0.0.1:3000,http://127.0.0.1:3001" >> $FILE
echo SECRET_KEY="dsijfdsojfhd*&@)*^!@(*#^@!*(&YSHdhaskjk" >> $FILE
echo CSRF_TRUSTED_ORIGINS="http://127.0.0.1:3000, http://127.0.0.1:3001, https://127.0.0.1.:8000/, http://192.168.31.203, http://127.0.0.1" >> $FILE

echo "Переменные окружения установлены"
}

if [ -f "$FILE" ]; then
    rm $FILE
fi

setup_env