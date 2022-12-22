from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl
import time
import urllib
import pandas as pd

contatos_df = pd.read_excel("mailing.xlsx")
#display(contatos_df)

# sistema cria uma "macro" para enviar mensagem de maneira automatizada
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len (navegador.find_elements("id","side")) < 1:
    time.sleep(1)

# neste momento o WhatsApp web deve estar com login efetuado

for i, mensagem in enumerate(contatos_df["mensagem"]):
    pessoa = contatos_df.loc[i, "pessoa"]
    numero = contatos_df.loc[i, "numero"]
    texto = urllib.parse.quote(f"Olá {pessoa}! {mensagem}")
    link =f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements("id","side"))<1:
        time.sleep(1)
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)
    time.sleep(10) 

# criar função apra pular caso o numero não tenha wpp.
