# Import the Selenium library
from selenium import webdriver

# Set the URL of the WhatsApp web page
whatsapp_url = "https://web.whatsapp.com/"

# Start a new Chrome webdriver
driver = webdriver.Chrome()

# Open the WhatsApp web page
driver.get(whatsapp_url)

# Wait for the user to scan the QR code and log in
input("Press Enter after you have scanned the QR code and logged in...")

# Find all the messages on the page
messages = driver.find_elements_by_class_name("_3_7SH")

# Print the messages
for message in messages:
    print(message.text)
