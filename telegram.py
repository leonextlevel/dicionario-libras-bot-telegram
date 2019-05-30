import telebot
from scraping import *


bot_token = '701005414:AAGUfx_l4M33Pftx_AnTllMc4_jtmICS-Xk'

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def msg_start(message):
        bot.reply_to(message, '''DICIONÁRIO DE LIBRAS

Olá, sou o bot de Libras, comigo você tem acesso a milhares de sinais em libras de diversas palavras do português brasileiro.

Espero ser muito útil e em caso de problemas entre em contato com meu pai através de seu e-mail:
librasbot@gmail.com

VAMOS COMEÇAR!!!

Para isso use um dos comandos que disponibilizo.

Comandos

/help - para receber ajudar a qualquer momento
/libras <palavra> - digite a palavra desejada no lugar de <palavra> para buscar o sinal em libras dela.''')


@bot.message_handler(commands=['help'])
def msg_bv(message):
        bot.reply_to(message, '''ESTÁ COM DIFICULDADES?! :(
Use ''')


@bot.message_handler(commands=['libras'])
def comando_libra(message):
        comando = message.text.split(' ')
        try:
                bot.reply_to(message, 'Estou procurando esta palavra, por favor aguarde!')
                bot.reply_to(message, gerar_link(comando[1]))
        except IndexError:
                bot.reply_to(message, 'Palavra indisponível')

while True:
        bot.polling()
