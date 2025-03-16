import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Define Variables
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
Password = "secret_sauce"
Wait_time = 2

# Launch Chrome Browser using selenium webdriver
driver = webdriver.Chrome()

# Navigate to the Login Page
driver.get(URL)
driver.maximize_window()
time.sleep(Wait_time)

# Enter Username
driver.find_element(By.ID, "user-name").send_keys(USERNAME)
time.sleep(Wait_time)

# Input Valid Password
driver.find_element(By.ID,"password").send_keys(Password)
time.sleep(Wait_time)

# Click Login Button
driver.find_element(By.ID,"login-button").click()
time.sleep(Wait_time)

# Add Product to the Cart

# Click on Sauce Labs Backpack Add to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(Wait_time)

# Click on Sauce Labs Bike Light Add to Cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(Wait_time)

# Click on Sauce Labs Fleece Jackets Add to Cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(Wait_time)

# Click on Sauce Labs Onesie Add to Cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
time.sleep(Wait_time)

# Click on T-Shirt (Red) Add to Cart
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(Wait_time)

# Click on Sauce Labs Bolt T-Shirt Add to Cart
# driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
# time.sleep(Wait_time)

# Click Checkout
# driver.find_element(By.ID, "checkout").click()
# time.sleep(Wait_time)

# Click Logout
# driver.find_element(By.ID, "logout_sidebar_link").click()
# time.sleep(Wait_time)