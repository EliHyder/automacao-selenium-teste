from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://the-internet.herokuapp.com/login'
site = webdriver.Chrome()
site.get(url=url)

campo_usuario = site.find_element(By.ID, 'username')
campo_usuario.send_keys('tomsmith')
time.sleep(2)
campo_senha = site.find_element(By.ID, 'password')
campo_senha.send_keys('SuperSecretPassword!')
time.sleep(2)
botao_login = site.find_element(By.CSS_SELECTOR, 'i.fa.fa-2x.fa-sign-in')
botao_login.click()
time.sleep(5)
site.quit()