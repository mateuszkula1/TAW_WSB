import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgSearch(unittest.TestCase):
    # If a script has the setUp() method defined, then the runner will call it 
    # first before running any of the test handlers.
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://wizzair.com/#/")

    #  tearDown() lets us clean the values initialized at the beginning of test via setUp() method.
    # def tearDown(self):
    #     self.browser.quit()

    # Testcase
    def test_wizzair_com_email_register(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pill")))
        # Click "sign in" button
        self.browser.find_element_by_xpath('/html/body/div[1]/header/div[1]/div/nav/ul/li[7]/button').click()
        # Click "Register" button
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[7]/section/form/div/p/button')))
        self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[7]/section/form/div/p/button').click()
        # Type in wrong e-mail address
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[10]/section/form/div[2]/div[5]/div[1]/label/input')))
        emailWindow = self.browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[10]/section/form/div[2]/div[5]/div[1]/label/input')
        emailWindow.clear()
        emailWindow.send_keys("wrong_mail")
        emailWindow.send_keys(Keys.RETURN)
        # Check if correct error message occured
        assert "Invalid e-mail" in self.browser.page_source
if __name__ == "__main__": unittest.main()