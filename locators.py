from selenium.webdriver.common.by import By



class SearchResultPageLocators:
    
    TIN = (By.ID, 'tin')
    
    CAPTCHA_TEXT = (By.ID, 'captcha') # Read 
    
    CAPTCHA = (By.ID, 'txt_Captcha') 
    
    REFRESH = (By.ID, 'refresh')
    
    SUBMIT = (By.ID, 'tinSubBtn')
    
    STATUS = (By.XPATH, '//*[@id="msg"]')

    TAX_PAYER_NAME = (By.XPATH, '//*[@id="tin_result"]/div/div[2]')

    
    
    
    