import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_button_is_present(language, browser):
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    assert EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")), "Button is not visible"



