"""
 Name : Harish kumar
 Date : 19-Oct-2024
 Program 1 : Using python selenium automation display the cookie created before login and after the login in the console.after you login in the dashboard of the portal kindly do logout also.
 verify that cookies are being generated during login process. 
 """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

try:
    # Navigate to the Sauce Demo login page
    driver.get('https://www.saucedemo.com/')

    # Display cookies before login
    cookies_before_login = driver.get_cookies()
    print("Cookies before login:")
    print(cookies_before_login)

    # Locate the username and password fields and login button
    username_input = driver.find_element(By.ID, 'user-name')
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

    # Input credentials and log in
    username_input.send_keys('standard_user')  
    password_input.send_keys('secret_sauce')   
    login_button.click()

    # Wait for the dashboard to load
    time.sleep(3)

    # Display cookies after login
    cookies_after_login = driver.get_cookies()
    print("Cookies after login:")
    print(cookies_after_login)

    # Perform logout
    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    menu_button.click()
    time.sleep(1)
    
    logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
    logout_button.click()

    # Wait for logout 
    time.sleep(3)

    # Display cookies after logout
    cookies_after_logout = driver.get_cookies()
    print("Cookies after logout:")
    print(cookies_after_logout)

finally:

    driver.quit()
