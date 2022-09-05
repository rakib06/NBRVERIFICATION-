from bot.base import BasePage
from bot.locators import SearchResultPageLocators



class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(SearchResultPageLocators.URL)
        self.driver.maximize_window()
       
    def set_TIN(self, tin):
        self.driver.refresh()
        self.get_element(*SearchResultPageLocators.TIN).send_keys(tin)
    
    def get_captcha(self):
        self.captcha = self.get_element(*SearchResultPageLocators.CAPTCHA_TEXT).text
        return self.captcha
    
    def set_captcha(self):
        self.get_element(*SearchResultPageLocators.CAPTCHA).send_keys(self.captcha)
    
    def submit(self):
        self.get_element(*SearchResultPageLocators.SUBMIT).click()

    def refresh(self):
        self.get_element(*SearchResultPageLocators.REFRESH).click()

    def get_taxpayer_name(self):
        name = self.get_element(*SearchResultPageLocators.TAX_PAYER_NAME).text
        return name
    
    def get_status(self):
        status = self.get_element(*SearchResultPageLocators.STATUS).text
        return status

   