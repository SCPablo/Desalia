from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

frases = ["Se que no, pero y si sí...",
          "Mientras haya un 1% de probabilidades hay un 99% de fe",
          "Vamos con todísimo"
]



# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

# Navigate to a page where the textarea element exists
# Make sure the webpage with the textarea is already open in your Chrome browser
driver.get('https://www.instagram.com/p/C5TGloEo6fk/')  # Replace 'https://example.com' with the actual URL

# Find and click the "Rechazar cookies opcionales" button
try:
    # Wait for the button to be clickable (if it's not immediately available)
    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Rechazar cookies opcionales")]')))
    button.click()
except:
    print("Button not found or unable to click")

import time
import random

time.sleep(60)

colegazos = ["@XXXXX", "@XXXXXX"]

counter = 0
for i in range(0, 40):
    # Find the textarea element
    try:
        textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Añade un comentario..."]')))
        # Write text into the textarea
        text = random.choice(colegazos) + " " + random.choice(frases)
        textarea.send_keys(text)
    except:
        print("Textarea element not found")
        
    
    time.sleep(random.random())
    time.sleep(10)

    # Find and click the "Publicar" button
    try:
        publicar_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "x1i10hfl") and contains(text(), "Publicar")]')))
        publicar_button.click()
    except:
        print("Publicar button not found or unable to click")
        textarea.clear()
        counter -= 1

    time.sleep(random.random())
    time.sleep(8)