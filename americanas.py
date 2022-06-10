from selenium import webdriver
import time

navegador = webdriver.Chrome()
time.sleep(5)
navegador.maximize_window()
navegador.get('https://ri.americanas.com/informacoes-aos-investidores/central-de-resultados/')
navegador.find_element_by_xpath('//*[@id="lang-pt-br"]/div[2]/div/div').click()
navegador.find_element_by_xpath('//*[@id="lang-pt-br"]/main/div[2]/ul/li[2]/a').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="tabela_1"]/tbody/tr[1]/td[2]/a/img').click()