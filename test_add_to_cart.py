from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



def test_add_to_cart():
    # הגדרת דפדפן (לדוג' Chrome)
    driver = webdriver.Chrome()  # עדכן את הנתיב ל-chromedriver שלך

    # פתיחת האתר
    driver.get("https://www.saucedemo.com/")

    # הזנת שם משתמש וסיסמה כדי להיכנס
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # חכה שהדף ייטען (נכון לדף הבית של האתר לאחר התחברות)
    time.sleep(3)

    # חיפוש המוצר Sauce Labs Backpack ולחיצה על כפתור הוספה לעגלה
    product_add_button = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']/following-sibling::div/button")
    product_add_button.click()

    # חכה מספר שניות כדי לוודא שהמוצר הוסף לעגלה
    time.sleep(2)

    # בדוק אם העגלה אכן מכילה את המוצר
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    # חכה לטעינת העגלה
    time.sleep(2)

    # בדוק אם המוצר נמצא בעגלה
    product_in_cart = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    assert product_in_cart is not None, "המוצר לא נמצא בעגלה"

    print("המוצר הוסף לעגלה בהצלחה!")

    # סגירת הדפדפן
    driver.quit()

     