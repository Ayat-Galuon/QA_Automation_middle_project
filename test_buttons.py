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

class TestButtonhomepage():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1070, 660)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
# Test that the shopping cart page displays after clicking the cart.
  def test_buttoncard(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"secondary-header\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Your Cart"
    self.driver.close()

  # Test that the Checkout: Your Information page displays after clicking the Checkout.
  def test_button_checkout(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(2)
    #self.driver.switch_to.alert.accept()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"secondary-header\"]").text == "Checkout: Your Information"
    self.driver.close()


  # Test is to verify that clicking "Continue Shopping" redirects the user back to the home page.
  def test_button_continue_shop(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"secondary-header\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue-shopping\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Products"
    self.driver.close()

  #Test is to verify that clicking "Login" opens the home page for the user.
  def test_buttonlogin(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Products"
    self.driver.close()
  
  #Test is to verify that clicking "List" opens the burger menu.
  def test_button_itemlist(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-sidebar-link\"]").text == "All Items"
    self.driver.close()


  # Test that the user is logged out and redirected to the login page after clicking 'Logout'
  def test_button_logout(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"logout-sidebar-link\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, ".login_logo").text == "Swag Labs"
    self.driver.close()

  #Test that the user is redirected to the login page after clicking 'Logout'.
  def test_button_finishcancel(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("sara")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("aljlad")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("8495000")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"cancel\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Products"
    self.driver.close()
  
  #Test the successful completion of the checkout process after clicking 'finish'.
  def test_button_finish(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("sara")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("aljlad")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("8495000")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"complete-header\"]").text == "Thank you for your order!"
    self.driver.close()

  #Test that clicking the "Cancel" button in checkout returns the user to the home page.
  def test_button_continueCheckoutcancel(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("sara")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("aljlad")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("8495000")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"cancel\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Products"
    self.driver.close()
    
  # Test that clicking "Continue" navigates to the "Checkout: Overview" page.
  def test_button_continueCheckout(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("sara")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("aljlad")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("8495000")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Checkout: Overview"
    self.driver.close()
  
  # Test that clicking "Back to Products" navigates to the home page.
  def test_button_backhome(self):
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("sara")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("aljlad")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("8495000")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Products"
    self.driver.close()
  
  
