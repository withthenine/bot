from selenium import webdriver
from selenium.webdriver.common.by import By  
import time
# Initialize the WebDriver instance
driver = webdriver.Chrome()  # or pass service=s if you want to use a specific ChromeDriver executable

# Navigate to the URL
driver.get("https://github.com/withthenine")

# Wait for 2 seconds
time.sleep(8)

# Find the element using XPath

button = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[2]/div/div[2]/turbo-frame/div/div[1]/div/ol/li[2]/div/div/div/span[1]/a/span")
button.click()
# Wait for 2 seconds
time.sleep(4)


