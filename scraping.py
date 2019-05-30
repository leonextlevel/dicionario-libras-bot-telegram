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
        driver.find_element_by_xpath(f"//*[text()='{palavra.upper()}']").click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(3)
        gif = soup.source.get('src')
        link = "http://www.acessibilidadebrasil.org.br/libras_3/" + gif
        return('''ENCONTREI ELA... ( ͡° ͜ʖ ͡°)

Palavra: {palavra}

Disponível em: {link}'''.format(palavra=palavra.upper(), link=link))
