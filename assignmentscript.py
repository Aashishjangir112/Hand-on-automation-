from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time


chrome_driver_path = r'C:\Users\aashi\PycharmProjects\chromedriver-win64/chromedriver.exe'

# Create a Chrome webdriver instance with Service
ser_obj = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser_obj)
driver.get("file:///C:/Users/aashi/assignment/assignment.html")  # Replace with the actual file path

# Define a function to wait for an element to be present
def wait_for_element_present(selector):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

time.sleep(2)

# Interact with elements
wait_for_element_present("#name")
name_input = driver.find_element("id", "name")
name_input.send_keys("Aashish")

time.sleep(2)  # Add a 10-second sleep

wait_for_element_present("#address")
address_textarea = driver.find_element("id", "address")

time.sleep(2)  # Add a 10-second sleep

wait_for_element_present("#subscribe")
subscribe_checkbox = driver.find_element("id", "subscribe")
subscribe_checkbox.click()

time.sleep(2)  # Add a 10-second sleep

wait_for_element_present("#male")  # Assuming Male is selected
gender_radio = driver.find_element("id", "male")
gender_radio.click()

time.sleep(2)  # Add a 10-second sleep

wait_for_element_present("#country")
country_dropdown = driver.find_element("id", "country")
country_dropdown.send_keys("INDIA")  # Sending keys to select the option

time.sleep(2)  # Add a 10-second sleep

# Submit the form
wait_for_element_present("button[type='submit']")
submit_button = driver.find_element("xpath", "//button[@type='submit']")
submit_button.click()

# Wait for a bit for the alert to appear
time.sleep(2)

# Print confirmation message
alert = driver.switch_to.alert
print("Form submitted successfully! Alert message: ", alert.text)

# Close the alert
alert.accept()

# Close the browser
driver.quit()

