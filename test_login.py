import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMessageError():
  def setup_method(self, method):
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Firefox()
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1070, 660)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  # Test the login functionality with incorrect username and password.
  @pytest.mark.parametrize("user_name, Password, message_error", [
    ("visual_user", "ghgh", "Epic sadface: Username and password do not match any user in this service"),  # Valid username, incorrect password
    ("visual_user", "", "Epic sadface: Password is required"),  # Valid username, empty password
    ("", "secret_sauce", "Epic sadface: Username is required"),  # empty username, valid password
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),  # Locked out user
    ("", "", "Epic sadface: Username is required")  # Empty fields
   ])
  
  def test_login_invalid_user(self, user_name, Password, message_error):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys(user_name)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(Password)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(2)
    assert self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3").text == str(message_error)
    self.driver.close()

