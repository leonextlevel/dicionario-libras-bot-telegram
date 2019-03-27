import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup


browser = webdriver.Firefox(executable_path="./geckodriver")
browser.set_window_size(100,100)
browser.set_window_position(0,0)
time.sleep(2)
browser.get("http://www.acessibilidadebrasil.org.br/libras_3/")
browser.implicitly_wait(20)

browser.find_element_by_xpath('//*[@id="search_field"]').click()
browser.find_element_by_xpath('//*[@id="search_field"]').send_keys("Laranja")
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[4]/td/input').click()
browser.find_element_by_xpath('//*[@id="0"]').click()
browser.find_element_by_xpath('//*[@id="0"]').send_keys(u'\ue015')


site = "http://www.acessibilidadebrasil.org.br/libras_3/"
page = urlopen(site)
soup = BeautifulSoup(page, 'html.parser')

imagem = soup.img.get('src')
link = "http://www.acessibilidadebrasil.org.br/libras_3/"+imagem
print(link)