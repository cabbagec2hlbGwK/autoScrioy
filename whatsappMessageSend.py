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

# Set the recipient's name
recipient_name = "John Doe"

# Find the recipient's chat in the chat list
chat = driver.find_element_by_xpath(f"//span[@title='{recipient_name}']")

# Click on the recipient's chat to open it
chat.click()

# Set the message you want to send
message = "Hello, world!"

# Find the input field for writing messages
input_field = driver.find_element_by_class_name("_1Plpp")

# Type the message into the input field
input_field.send_keys(message)

# Find the send button
send_button = driver.find_element_by_class_name("_35EW6")

# Click on the send button to send the message
send_button.click()

# Print a success message
print(f"Sent message to {recipient_name}")
