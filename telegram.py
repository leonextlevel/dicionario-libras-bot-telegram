import telebot
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup

def gerar_link(palavra):

	browser = webdriver.Firefox(executable_path="./geckodriver")
	browser.set_window_size(100,100)
	browser.set_window_position(0,0)
	time.sleep(2)
	browser.get("http://www.acessibilidadebrasil.org.br/libras_3/")
	browser.implicitly_wait(20)

	browser.find_element_by_xpath('//*[@id="search_field"]').click()
	browser.find_element_by_xpath('//*[@id="search_field"]').send_keys(palavra)
	browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[4]/td/input').click()
	browser.find_element_by_xpath('//*[@id="0"]').click()
	browser.find_element_by_xpath('//*[@id="0"]').send_keys(u'\ue015')


	site = "http://www.acessibilidadebrasil.org.br/libras_3/"
	page = urlopen(site)
	soup = BeautifulSoup(page, 'html.parser')

	time.sleep(3)

	imagem = soup.img.get('src')
	link = "http://www.acessibilidadebrasil.org.br/libras_3/"+imagem
	return('''
Palavra: {palavra}
imagem: {link}'''.format(palavra=palavra, link=link))

bot_token = '701005414:AAGUfx_l4M33Pftx_AnTllMc4_jtmICS-Xk'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def msg_bv(message):
	bot.reply_to(message, 'DICIONARIO DE LIBRAS\n Digite /help para receber ajudar!')

@bot.message_handler(commands=['help'])
def msg_bv(message):
	bot.reply_to(message, '"/libra <palavra>" para receber uma imagem de como é executado o sinal em libras da palavra.')

@bot.message_handler(commands=['libra'])
def comando_libra(message):
	comando = message.text.split(' ')
	try:
		bot.reply_to(message, gerar_link(comando[1]))
	except IndexError:
		bot.reply_to(message, 'Palavra indisponível')
bot.polling()