import random
import logging
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


# Configure logging
logging.basicConfig(filename='script_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


logging.info('Script started')

# Set up Firefox options
firefox_options = Options()
firefox_options.headless = False  # Run Firefox in headless mode, set to False for visible browser

# Set up Firefox WebDriver
gecko_path = "/Users/pablo/geckodriver/geckodriver"  # Path to geckodriver executable
service = Service(gecko_path)

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open the webpage
url = "https://desalia.barceloviveahora.com/login"
driver.get(url)

# Wait for the page to load
time.sleep(3)  # Adjust as needed, depending on the page load time


# Find the "Correo electrónico" input field and fill it with the email
try:
    email = "XXXXXXXXXXXXX"
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
    password = "XXXXXXXX"
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
    entrar_button = driver.find_element(By.XPATH, "//button[contains(text(),'Entrar')]")
    entrar_button.click()
    print("Clicked on 'ENTRAR' button")
except Exception as e:
    print("Failed to click on 'ENTRAR' button:", e)
    logging.error("ERROR: Failed to click on 'ENTRAR' button:")



time.sleep(2)


for i in range(162):
    # Find the input field and fill it with "AAAA"
    try:
        duck_name = 'Roni te prometo que este año no he hecho un bot'
        input_field = driver.find_element(By.ID, "patito_name")
        input_field.clear()  # Clear any existing value
        input_field.send_keys(duck_name)
        print("Filled the field with " + duck_name)
    except Exception as e:
        print("Failed to fill the field with: " + duck_name)
        logging.error("Failed to fill the field with: " + duck_name)



    time.sleep(1)

    # Click the "JUGAR" button
    try:
        jugar_button = driver.find_element(By.ID, "play-again-button")
        jugar_button.click()
        print("Clicked on 'JUGAR' button")
    except Exception as e:
        print("Failed to click on 'JUGAR' button:", e)
        logging.error("ERROR: ailed to click on 'JUGAR' button:", e)


    time.sleep(3)

    # Find the image element and click on it
    try:
        image = driver.find_element(By.CLASS_NAME, "game-btn")
        image.click()
        print("Clicked on the image")
    except Exception as e:
        print("Failed to click on the image:", e)
        logging.error("ERROR: Failed to fill 'Contraseña' field with password:", e)


    time.sleep(5)

    # Simulate pressing the space key twice
    try:
        action_chains = ActionChains(driver)

        jumps = random.randint(0, 8)
        for i in range(jumps):
            action_chains.send_keys(Keys.SPACE).perform()
            time.sleep(0.1 * random.randint(1, 5))
        
        time.sleep(jumps*1)
        print("Jumped")
    except Exception as e:
        print("Failed to jump:", e)
        logging.error("ERROR: Failed to jump")



    time.sleep(2)

    # Click on the "VOLVER A JUGAR" button
    try:
        volver_a_jugar_button = driver.find_element(By.ID, "play-again-button")
        volver_a_jugar_button.click()
        logging.info("Se ha completado un intento")
        print("Clicked on the 'VOLVER A JUGAR' button")
    except Exception as e:
        print("Failed to click on the 'VOLVER A JUGAR' button:", e)
        logging.error("ERROR: Failed to click on the 'VOLVER A JUGAR' button", e)


    time.sleep(5)

logging.info("Script ended")


