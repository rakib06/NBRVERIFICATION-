from bot.search_page import SearchPage
from bot import driver_setup
from utils.log import log_manager

TINs = [
    361465492546,
    584863325031,
    886860634157,
    511637851504,
    137145394101,
    212321650378,
    785749199735
    
]

logger = log_manager.app_logger()


driver = driver_setup.local()

x = SearchPage(driver)
# driver.maximize_window()


try:
    for tin in TINs:
        x.set_TIN(tin)
        captcha = x.get_captcha()
        x.set_captcha()
        x.submit()
        status = x.get_status()
        tax_payer_name = x.get_taxpayer_name()
        logger.info(f"\n{tax_payer_name}\nTIN: {tin}, Captcha: {captcha}\nStatus: {status}\n\n")
    

except Exception as e:
    logger.error(e)
    driver.save_screenshot()

finally:
    
    driver.quit()