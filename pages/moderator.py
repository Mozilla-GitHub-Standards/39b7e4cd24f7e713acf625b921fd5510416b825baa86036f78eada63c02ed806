from selenium.webdriver.common.by import By

from pages.base import Base


class Moderator(Base):
    _login_button_locator = (By.CSS_SELECTOR, 'a[class="login btn btn-primary"]')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[href="/oidc/logout/"]')

    @property
    def is_logout_button_displayed(self):
        return self.is_element_visible(*self._logout_button_locator)

    def click_sign_in_button(self):
        self.selenium.find_element(*self._login_button_locator).click()

    def click_logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()
