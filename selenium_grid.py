#import time
#from selenium.webdriver.fireFox.options import Options as FirefoxOptions  
#from selenium import webdriver

#Options = FirefoxOptions ()
#Options.set_capability("browserName", "firefox")
#Options

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

options=ChromeOptions()
options.set_capability("browserName","chrome")
options.set_capability("browserVersion","latest")
options.set_capability("platformName","Windows")

driver=webdriver.Remote("http://localhost:4444/wd/hub",options=options)



service=ChromeService(ChromeDriverManager().install())
driver=webdriver.Chrome()
#driver=webdriver.Edge()

driver.get("https://automationexercise.com/")
driver.set_window_size(1536,808)