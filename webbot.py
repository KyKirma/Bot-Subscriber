# Importando o webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Instanciando o Objeto ChromeOptions
options = webdriver.ChromeOptions()

# Passando algumas opções para esse ChromeOptions
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-crash-reporter')
options.add_argument('--log-level=3')
options.add_argument('--disable-gpu')
options.add_experimental_option('detach', True)

# Criando o driver "bot"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Bibliotecas extras
from tqdm import tqdm
import time

driver.get("https://portalcarreira.propagandistadeprimeira.com.br/auth/login")

# Processo de login no site
checkBoxLogin = driver.find_elements(By.CSS_SELECTOR, 'label.custom-control-label') #Acha as checkboxs do site

recrutadorButton = checkBoxLogin[1] #Seleciona a opção do recrutador
recrutadorButton.click() 

info = {'login' : 'Admin@gmail.com',
         'senha' : 'root'}

emailEntry = driver.find_element(By.NAME, 'email') #Seleciona o email
emailEntry.send_keys(info['login']) #Adiciona ao campo
passwordEntry = driver.find_element(By.NAME, 'password')
passwordEntry.send_keys(info['senha'])

loginButton = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
loginButton.click()

time.sleep(5)
