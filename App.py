import telebot
import requests
import json
import datetime
from Config.Settings import API_URL, TOKEN_TELEBOT


bot = telebot.TeleBot(TOKEN_TELEBOT)


def log(message):
    tanggal = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    namaAwal = message.chat.first_name
    namaAkhir = message.chat.last_name
    username = message.chat.username
    textLog = '{}|{} - {} {}, {} \n'.format(
        tanggal, username, namaAwal, namaAkhir, message.text)
    print(textLog)
    logger = open('logger.txt', 'a')
    logger.write(f'{textLog} \n')
    logger.close()


def removePrefix(text):
    try:
        return text.split(' ', 1)[1]
    except:
        return " "


@bot.message_handler(commands=['query'])
def query(message):
    log(message)
    nlParam = removePrefix(message.text)
    api_unsribot = requests.post(
        f'{API_URL}?nlParam={nlParam}')
    api_unsribot = api_unsribot.json()
    result = api_unsribot["query"]
    bot.reply_to(message, result)


@bot.message_handler(commands=['detail'])
def detail(message):
    log(message)
    nlParam = removePrefix(message.text)
    api_unsribot = requests.post(
        f'{API_URL}?nlParam={nlParam}')
    api_unsribot = api_unsribot.json()
    result = f"""
Token: 
{api_unsribot["kalimat"]}

Kalimat Perintah:
{api_unsribot["isPerintah"]}

Tabel:
{api_unsribot["identifikasiTabel"]}

Kolom Tabel: 
{api_unsribot["identifikasiKolomByTabel"]}

Kondisi: 
{api_unsribot["identifikasiKondisi"]}

Kolom Kondisi: 
{api_unsribot["identifikasiKolomKondisi"]}

Atribut Kondisi:
{api_unsribot["identifikasiAtributKondisi"]}

Operator:
{api_unsribot["identifikasiOperator"]}

Query:
{api_unsribot["query"]}
    """
    bot.reply_to(message, result)


def main():
    print('telebot unsribot running')
    bot.infinity_polling(timeout=10, long_polling_timeout=5)


if __name__ == '__main__':
    main()
