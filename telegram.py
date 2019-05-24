import telebot
from selenium import webdriver
import time
from bs4 import BeautifulSoup


def gerar_link(palavra):
        driver = webdriver.PhantomJS()
        driver.get("http://www.acessibilidadebrasil.org.br/libras_3/")
        driver.implicitly_wait(10)

        driver.find_element_by_xpath('//*[@id="search_field"]').click()
        driver.find_element_by_xpath('//*[@id="search_field"]').send_keys(palavra)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[4]/td/input').click()
        driver.find_element_by_xpath('//*[@id="0"]').click()
        driver.find_element_by_xpath('//*[@id="0"]').send_keys(u'\ue015')

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(3)
        gif = soup.source.get('src')
        link = "http://www.acessibilidadebrasil.org.br/libras_3/" + gif
        return('''
Palavra: *{palavra}*

imagem: {link}'''.format(palavra=palavra.upper(), link=link))


bot_token = '701005414:AAGUfx_l4M33Pftx_AnTllMc4_jtmICS-Xk'

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def msg_bv(message):
	bot.reply_to(message, '''DICIONÁRIO DE LIBRAS

Olá, sou o bot de Libras, comigo você tem acesso a milhares de sinais em libras de diversas palavras do português brasileiro.

Espero ser muito útil e em caso de problemas entre em contato com meu pai através de seu e-mail:
librasbot@gmail.com

VAMOS COMEÇAR!!!

Para isso use um dos comandos que disponibilizo.

Comandos

/help - para receber ajudar a qualquer momento
/libra <palavra> - para buscar o sinal em libras da palavra deseja''')


@bot.message_handler(commands=['help'])
def msg_bv(message):
	bot.reply_to(message, '''ESTÁ COM DIFICULDADES?! :(
Use ''')


@bot.message_handler(commands=['libra'])
def comando_libra(message):
	comando = message.text.split(' ')
	try:
		bot.reply_to(message, gerar_link(comando[1]))
	except IndexError:
		bot.reply_to(message, 'Palavra indisponível')
bot.polling()
