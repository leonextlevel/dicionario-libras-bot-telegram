from urllib.request import urlopen
from bs4 import BeautifulSoup

site = "http://www.acessibilidadebrasil.org.br/libras_3/"

page = urlopen(site)

soup = BeautifulSoup(page, 'html.parser')

print(soup.title)