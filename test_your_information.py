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

class TestYourInformation():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1070, 660)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  # Test that the checkout page accepts valid information.
  def test_validin_formation(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("sara")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("aljald")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("05890000")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart_footer").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Checkout: Overview"
    self.driver.close()
  

  # Test that the checkout page does not proceed without entering the first name.
  def test_missing_first_name(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("aljald")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("05890000")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Error: First Name is required"
    time.sleep(2)
    self.driver.close()


  #Test that the checkout page does not proceed without entering the last name.
  def test_missing_last_name(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("sara")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("05890000")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Error: Last Name is required"
    time.sleep(2)
    self.driver.close()


  #Test that the checkout page does not proceed without entering the postal code.
  def test_missing_posta_code(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("sara")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("aljlad")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Error: Postal Code is required"
    time.sleep(2)
    self.driver.close()


  #Test that the checkout page does not proceed without entering all the information.
  def test_empty_fields(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Error: First Name is required"
    time.sleep(2)
    self.driver.close()
