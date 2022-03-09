import telebot
import requests
import json
from Config.Settings import API_URL, TOKEN_TELEBOT

bot = telebot.TeleBot(TOKEN_TELEBOT)


def removePrefix(text):
    return text.split(' ', 1)[1]


@bot.message_handler(commands=['query'])
def query(message):
    nlParam = removePrefix(message.text)
    api_unsribot = requests.post(
        f'{API_URL}?nlParam={nlParam}')
    api_unsribot = api_unsribot.json()
    result = api_unsribot["query"]
    bot.reply_to(message, result)


@bot.message_handler(commands=['detail'])
def detail(message):
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


print('telebot unsribot running')
bot.polling()
