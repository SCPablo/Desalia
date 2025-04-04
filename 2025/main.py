import random
import logging
import datetime
import json 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


# Configure logging
logging.basicConfig(
    filename='2025/script_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


logging.info('Script started')

# Cargar credenciales desde config.json
config_path = "2025/config.json"
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

email = config.get("user")
password = config.get("password")


nombres_path = "2025/nombres.txt"
with open(nombres_path, 'r') as nombres_file:
    nombres = [line.strip() for line in nombres_file.readlines()]



# Set up Firefox options
firefox_options = Options()
firefox_options.headless = False  # Run Firefox in headless mode, set to False for visible browser

# Set up Firefox WebDriver
gecko_path = "/Users/pablo/geckodriver/geckodriver"  # Path to geckodriver executable
service = Service(gecko_path)

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open the webpage
url = "https://desaliaviveahora.com/login?_gl=1*y1kldp*_up*MQ..*_ga*NDgyMTM2NjAuMTc0MzcwMzQ4MQ..*_ga_2C5W1V2S8T*MTc0MzcwMzQ3OS4xLjAuMTc0MzcwMzQ3OS4wLjAuMTM1NzMxMTU2NQ.."
driver.get(url)

# Wait for the page to load
time.sleep(3)  # Adjust as needed, depending on the page load time


# Find the "Correo electrónico" input field and fill it with the email
try:
    email_input = driver.find_element(By.ID, "email")
    email_input.clear()  # Clear any existing value
    email_input.send_keys(email)
    print("Filled 'Correo electrónico' field with email")
except Exception as e:
    print("Failed to fill 'Correo electrónico' field with email:", e)
    logging.error("ERROR: Failed to fill 'Correo electrónico' field with email")


time.sleep(1)


# Find the "Contraseña" input field and fill it with the password
try:
    pass_input = driver.find_element(By.ID, "password")
    pass_input.clear()  # Clear any existing value
    pass_input.send_keys(password)
    print("Filled 'Contraseña' field with password")
except Exception as e:
    print("Failed to fill 'Contraseña' field with password:", e)
    logging.error("ERROR: Failed to fill 'Contraseña' field with password:")



time.sleep(2)


# Click the "ENTRAR" button
try:
    entrar_button = driver.find_element(By.XPATH, "//button[contains(text(),'ENTRAR')]")
    entrar_button.click()
    print("Clicked on 'ENTRAR' button")
except Exception as e:
    print("Failed to click on 'ENTRAR' button:", e)
    logging.error("ERROR: Failed to click on 'ENTRAR' button:")



time.sleep(2)


for i in range(162):
    # Find the input field and fill it with "AAAA"
    try:
        duck_name = random.choice(nombres)
        input_field = driver.find_element(By.ID, "desalier_name")
        input_field.clear()  # Clear any existing value
        input_field.send_keys(duck_name)
        print("Filled the field with " + duck_name)
    except Exception as e:
        print("Failed to fill the field with: " + duck_name)
        logging.error("Failed to fill the field with: " + duck_name)



    time.sleep(3)

    # Click the "JUGAR" button
    try:
        jugar_button = driver.find_element(By.ID, "play-game-button")
        jugar_button.click()
        print("Clicked on 'JUGAR' button")
    except Exception as e:
        print("Failed to click on 'JUGAR' button:", e)
        logging.error("ERROR: ailed to click on 'JUGAR' button:", e)


    time.sleep(3)



    # Click on the "EXPLORA TODOS LOS PATOS ANTES DE QUE SE LLENE LA PANTALLA" button
    try:
        volver_a_jugar_button = driver.find_element(By.ID, "start")
        volver_a_jugar_button.click()
        logging.info("Jugando")
        print("Estamos jugando")
    except Exception as e:
        print("Failed to click on the 'JUGAR' button:", e)
        logging.error("ERROR: ailed to click on the 'JUGAR' button", e)


    time.sleep(33)


    # Click on the "VOLVER A JUGAR" button
    try:
        volver_a_jugar_button = driver.find_element(By.ID, "play-again-button")
        volver_a_jugar_button.click()
        logging.info("Se ha completado un intento")
        print("Clicked on the 'VOLVER A JUGAR' button")
    except Exception as e:
        print("Failed to click on the 'VOLVER A JUGAR' button:", e)
        logging.error("ERROR: Failed to click on the 'VOLVER A JUGAR' button", e)

    time.sleep(3)

logging.info("Script ended")


