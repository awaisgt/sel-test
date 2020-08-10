import os
from selenium import webdriver
op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"),op)
driver.get('https://www,google.com')
print(driver.page_source)