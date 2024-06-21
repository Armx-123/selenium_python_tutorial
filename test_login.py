from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get('https://www.example.com')

# Get the title of the page
title = driver.title

# Print the title
print(f"The title of the page is: {title}")

# Close the browser
driver.quit()
