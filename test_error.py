import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestError():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1070, 660)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  #This test is to verify that the checkout page displays the correct user information.

  def test_error1(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("problem_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".checkout_info").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("sara")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("aljlad")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("5465")
    time.sleep(2)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").text == "aljlad"
    self.driver.close() 

  #Test that the "Remove" button changes to "Add to cart" after removing an item.
  def test_error2(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("problem_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bike-light\"]").click()
    time.sleep(3)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bike-light\"]").text == "Add to cart"
    self.driver.close()



  def test_error3(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("problem_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").text == "Sauce Labs Backpack"
    self.driver.close()


  
