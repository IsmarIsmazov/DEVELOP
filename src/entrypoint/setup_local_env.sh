#!/bin/sh

FILE=../src/.env

function setup_env(){
echo "Устанавливаются переменные окружения"

echo "Переменные окружения установлены"
}

if [ -f "$FILE" ]; then
    rm $FILE
fi

setup_env