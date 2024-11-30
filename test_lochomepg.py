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

class TestLochomepage():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1070, 660)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  #Test that the product name for item on the homepage is correct.
  def test_product_name(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR,"*[data-test=\"inventory-item-name\"]").text == "Sauce Labs Backpack"
    time.sleep(1)
    self.driver.close()

  #Test that the product description is displayed correctly.
  def test_product_desc(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-desc\"]").text == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
    time.sleep(1)
    self.driver.close()
  
  #Test that the home page title displays "Swag Labs".
  def test_home_page_title(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".app_logo").text == "Swag Labs"
    time.sleep(1)
    self.driver.close()
  
  #Test that the page title displays "Products".
  def test_home_page_title2(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Products"
    time.sleep(1)
    self.driver.close()

  #Test that the price of product on the home page is displayed as "$29.99". 
  def test_home_page_coin(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-price\"]").text == "$29.99" 
    time.sleep(1)
    self.driver.close()

  
