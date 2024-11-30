import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time





#def test_login():
    #def setUp(self):
       # self.driver = webdriver.Chrome
      #  self.driver.get("https://www.saucedemo.com/")




  
class TestLoginSuite:

    def setup_method(self, method):
        # אתחול הדפדפן (למשל Chrome)
        self.driver = webdriver.Chrome  
        self.driver.get("https://www.saucedemo.com/")
        self.driver.set_window_size(1270, 660)  

    def teardown_method(self, method):
        # סגירת הדפדפן לאחר הבדיקה
        self.driver.quit()

    # בדיקה ללוגין עם פרטי משתמש תקינים
    def test_login_valid_user(self):
        # מציאת שדות שם משתמש, סיסמה וכפתור ההתחברות
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        # הזנת שם משתמש וסיסמה תקינים
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # המתן לטעינת עמוד המוצרים
        time.sleep(2)

        # בדוק אם הצלחנו להגיע לעמוד המוצרים
        inventory_list = self.driver.find_element(By.CLASS_NAME, "inventory_list")
        assert inventory_list.is_displayed(), "התחברות לא הצליחה - לא הגעת לעמוד המוצרים!"

    # בדיקה ללוגין עם פרטי משתמש שגויים
    @pytest.mark.parametrize("username, password, expected_message", [
        ("wrong_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
        ("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
        ("", "", "Epic sadface: Username is required")
    ])
    def test_login_invalid_user(self, username, password, expected_message):
        # מציאת שדות שם משתמש, סיסמה וכפתור ההתחברות
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        # הזנת שם משתמש וסיסמה שגויים
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # המתן להודעת השגיאה
        time.sleep(2)

        # בדוק אם הודעת השגיאה מוצגת
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert expected_message in error_message.text, f"ציפינו להודעה {expected_message}, אך קיבלו {error_message.text}"
 
