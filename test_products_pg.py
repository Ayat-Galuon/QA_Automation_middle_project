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

class TestProductspg():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1070, 660)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  # Test that the product name is correctly displayed on the product page.
  def test_prod_pg1(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").text == "Sauce Labs Backpack"
    self.driver.close()

  # Test that the "Back to products" button is correctly displayed on the product page.
  def test_prod_pg2(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").click()
    time.sleep(2)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").text == "Back to products"
    self.driver.close()

  # Test that the product description is correctly displayed on the product page.
  def test_prod_pg3(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").click()
    time.sleep(2)    
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-desc\"]").text == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
    self.driver.close()

  #Test that the product price is correctly displayed on the product page.
  def test_prod_pg4(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").click()
    time.sleep(2)  
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-price\"]").text == "$29.99"
    self.driver.close()

  # Test that the "Add to cart" button is correctly displayed on the product page.
  def test_prod_pg5(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").click()
    time.sleep(2)    
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart\"]").text == "Add to cart"
    self.driver.close()

  # Test that the img is displayed on the product page.
  def test_prod_pg6(self): 
   self.driver.find_element(By.CSS_SELECTOR, "*[data-test='username']").send_keys("standard_user")
   self.driver.find_element(By.CSS_SELECTOR, "*[data-test='password']").send_keys("secret_sauce")
   time.sleep(1)
   self.driver.find_element(By.CSS_SELECTOR, "*[data-test='login-button']").click()
   self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").click()
   time.sleep(2)
   image = self.driver.find_element(By.CSS_SELECTOR, '*[data-test="item-sauce-labs-backpack-img"]')
   assert image.get_attribute('alt') == "Sauce Labs Backpack"
   #assert image.get_attribute('src') != ""
   self.driver.close()