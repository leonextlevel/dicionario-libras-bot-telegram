import telebot
from scraping import *


bot_token = '701005414:AAGUfx_l4M33Pftx_AnTllMc4_jtmICS-Xk'

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def msg_start(message):
        bot.reply_to(message, '''DICIONÁRIO DE LIBRAS

Sou o bot de Libras, comigo você tem acesso a milhares de sinais em libras de diversas palavras do português brasileiro.

Espero ser muito útil e em caso de problemas entre em contato com meu criador através de seu e-mail:
leandro.bueno@fatec.sp.gov.br

VAMOS COMEÇAR!!!

Para isso use um dos comandos que disponibilizo.

Comandos:

/start - para ver essa mensagem novamente
/help - para receber ajuda a qualquer momento
/libras <palavra> - digite a palavra desejada no lugar de <palavra> para buscar o sinal em libras dela.''')


@bot.message_handler(commands=['help'])
def msg_bv(message):
        bot.reply_to(message, '''ESTÁ COM DIFICULDADES?! :(

É muito simples!

Digite /libras dê um espaço e digite a palavra que deseja buscar.

Exemplos:
/libras abacate
/libras computador

Tente você agora ;D''')


@bot.message_handler(commands=['libras'])
def comando_libra(message):
        comando = message.text.split(' ')
        try:
                bot.reply_to(message, 'Estou procurando esta palavra, por favor aguarde!')
                bot.reply_to(message, gerar_link(comando[1]))
        except Exception:
                bot.reply_to(message, 'Não consegui encontrá-la, me perdoe! :(')

bot.polling()

while True:
	pass
