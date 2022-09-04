TINs = [
    361465492546,
    584863325031,
    886860634157,
    511637851504,
    137145394101,
    212321650378,
    785749199735
    
]
from selenium.webdriver.support.ui import WebDriverWait

from utils.log import log_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
# from selenium.webdriver.chrome.options import Options
from locators import SearchResultPageLocators
logger = log_manager.app_logger()

def local():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

# def get_element(driver, *by):
   
#     element = WebDriverWait(driver, 30).until(lambda driver: driver.find_element(*by))
#     return element
driver = local()
driver.get("https://verification.taxofficemanagement.gov.bd/")
driver.maximize_window()
for tin in TINs:
    driver.find_element(*SearchResultPageLocators.TIN).send_keys(tin)
    captcha = driver.find_element(*SearchResultPageLocators.CAPTCHA_TEXT).text
    driver.find_element(*SearchResultPageLocators.CAPTCHA).send_keys(captcha)
    driver.find_element(*SearchResultPageLocators.SUBMIT).click()
    time.sleep(5)
    status = driver.find_element( *SearchResultPageLocators.STATUS).text
    print(status)
    logger.info(f"TIN: {tin},\n Status: {status}\n\n")
    
driver.close()