import random
import logging
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import json


def init_logging():
    logging.basicConfig(filename='script_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('Script started')


def set_up_firefox():
    firefox_options = Options()
    firefox_options.headless = False  # Run Firefox in headless mode, set to False for visible browser

    # Set up Firefox WebDriver
    gecko_path = "/Users/pablo/geckodriver/geckodriver"  # Path to geckodriver executable
    service = Service(gecko_path)

    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox(service=service, options=firefox_options)

    # Open the webpage
    url = "https://elafterdelverano.com/login"
    driver.get(url)
    
    return driver


def get_credentials():
    with open('config.json', 'r') as file:
        config = json.load(file)
        email = config['email']
        password = config['password']
    return email, password



def click_button(driver, name, pos):
    # Find the "Solicitar" button and click it
    try:
        # Encuentra el botón por su texto
        button = driver.find_elements(By.XPATH, "//button[contains(text()," + name + ")]")[pos]
        button.click()
        print("Clicked on " + name + " button")
    except Exception as e:
        print("Failed to click on " + name + " button:", e)
        logging.error("ERROR: Failed to click on" + name + " button:")


def first_page(driver):
    email, password = get_credentials()

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
    click_button(driver, "Entrar", 0)



def second_page(driver):
    time.sleep(3)
    # Desplaza hacia abajo en la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Scrolled down")
    time.sleep(2)
    # Click the "SOLCITAR" button
    try:
        solicitar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="SOLICITAR"]'))
        )
        solicitar_button.click()  # Haz clic en el botón
    except Exception as e:
        print("Failed to click on 'SOLICITAR' button:", e)
        logging.error("ERROR: Failed to click on 'SOLICITAR' button:")


def get_info(p1, p2, p3):
    try:
        with open('info.json', 'r') as file:
            info = json.load(file)
            return info[p1], info[p2], info[p3]
    except:
        return "Si", "Si", "Si"
    

def leer_questions(driver):
    pregunta1 = driver.find_element(By.XPATH, '//*[@id="question1"]/preceding-sibling::label').text
    pregunta2 = driver.find_element(By.XPATH, '//*[@id="question2"]/preceding-sibling::label').text
    pregunta3 = driver.find_element(By.XPATH, '//*[@id="question3"]/preceding-sibling::label').text

    # Imprime los resultados
    print("Pregunta 1:", pregunta1)
    print("Pregunta 2:", pregunta2)
    print("Pregunta 3:", pregunta3)

    answer1, answer2, answer3  = get_info(pregunta1, pregunta2, pregunta3)
    return answer1, answer2, answer3




def third_page(driver):

    time.sleep(2)
    answer1, answer2, answer3 = leer_questions(driver)
    
    try:
        # Espera hasta que el campo de la primera pregunta sea visible
        question1_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'question1'))
        )
        question1_input.send_keys(answer1)  # Reemplaza esto con la respuesta deseada

        time.sleep(1)

        # Espera hasta que el campo de la segunda pregunta sea visible
        question2_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'question2'))
        )
        question2_input.send_keys(answer2)  # Reemplaza esto con la respuesta deseada

        time.sleep(1)


        # Espera hasta que el campo de la tercera pregunta sea visible
        question3_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'question3'))
        )
        question3_input.send_keys(answer3)  # Reemplaza esto con la respuesta deseada

        time.sleep(2)

        # Encuentra el botón "OBTENER" y haz clic en él
        obtener_button = driver.find_element(By.XPATH, '//button[text()="OBTENER"]')
        obtener_button.click()

    except Exception as e:
        print("Failed to click on 'OBTENER' button:", e)
        logging.error("ERROR: Failed to click on 'OBTENER' button:")


def four_page(driver):
    time.sleep(2)
    try:
        # Espera hasta que el botón "CONTINUAR SIN FOTO" sea clickeable
        continuar_sin_foto_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "noPhotoLink"))
        )
        
        # Haz clic en el botón
        continuar_sin_foto_button.click()

    except Exception as e:
        print("Failed to click on 'CONTINUAR SIN FOTO' button:", e)
        logging.error("ERROR: Failed to click on 'CONTINUAR SIN FOTO' button:")


def last_page(driver):
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)


    try:
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.btn-landing")))
        # Hace clic en el botón
        button.click()

    except Exception as e:
        print("Failed to click on 'VUELVE A PARTICIPAR' button:", e)
        logging.error("ERROR: Failed to click on 'VUELVE A PARTICIPAR' button:")


# Configure logging
init_logging()

# Set up Firefox options
driver = set_up_firefox()


# Wait for the page to load
time.sleep(3)  # Adjust as needed, depending on the page load time


first_page(driver)
time.sleep(2)
second_page(driver)
time.sleep(2)

for i in range(20):
    third_page(driver)
    time.sleep(2)
    four_page(driver)
    time.sleep(15)
    logging.info("Application done")
    last_page(driver)
    time.sleep(5)


driver.quit()