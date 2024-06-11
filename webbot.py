# Importando o webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# Instanciando o Objeto ChromeOptions
options = webdriver.EdgeOptions()

# Passando algumas opções para esse ChromeOptions
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-crash-reporter')
options.add_experimental_option('detach', True)

# Criando o driver "bot"
driver = webdriver.Edge(options=options)

# Bibliotecas extras
import time

driver.get("https://portalcarreira.propagandistadeprimeira.com.br/auth/login")


# ====== Processo de login no site =========
checkBoxLogin = driver.find_elements(By.CSS_SELECTOR, 'label.custom-control-label') #Acha as checkboxs do site

recrutadorButton = checkBoxLogin[1] #Seleciona a opção do recrutador
recrutadorButton.click() 

info = {'login' : 'Admin@gmail.com',
         'senha' : 'root'}

emailEntry = driver.find_element(By.NAME, 'email') #Seleciona o email
emailEntry.send_keys(info['login']) #Adiciona ao campo
passwordEntry = driver.find_element(By.NAME, 'password')
passwordEntry.send_keys(info['senha'])

loginButton = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary') #Encontra o botão de login 
loginButton.click()
# ==========================================

time.sleep(5)

# === Processo de cadastro de candidatos ===
candidatoButton = driver.find_element(By.CSS_SELECTOR, "a[href*='/admin/add-user']") #Seleciona o botão de adicionar candidatos
candidatoButton.click()
time.sleep(3)

#? Puxaremos os campos de entrada para adicionar as info
userForm = driver.find_element(By.CSS_SELECTOR, 'form')
userNameEntry = driver.find_element(By.NAME, 'name')
userEmailEntry = driver.find_element(By.NAME, 'email')
userPhoneEntry = driver.find_element(By.NAME, 'celPhone')
userVitalicCheckbox = driver.find_elements(By.CSS_SELECTOR, 'label.form-check-label')
userVitalic = userVitalicCheckbox[0]
userTypeCheckbox = driver.find_elements(By.NAME, 'type')
userType = userTypeCheckbox[1]

#? adicionaremos nos campos as informações
userNameEntry.send_keys('João da silva teste')
userEmailEntry.send_keys('teste@gmail.com')
userPhoneEntry.send_keys('(34) 9 9999-9999')
userVitalic.click()
userType.click()
time.sleep(5)
userForm.submit()
# ==========================================

time.sleep(3)
