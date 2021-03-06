import unittest
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class KnowYourBrowsingHistory(unittest.TestCase):

    def setUp(self):
        chromepath = "C:/Users/bhagi/Downloads/chromedriver_win32/chromedriver.exe"
        #options=webdriver.ChromeOptions()
        #options.add_argument('headless')
        self.driver = webdriver.Chrome(chromepath)

    def test_know_your_browsing_history(self):

        driver = self.driver
        id, password, url =self.getValuesfromCSV('C:\\Users\\bhagi\\PycharmProjects\\APIFuzzer\propertyFile.csv')
        self.login(id,password,url)
        BrowserHistory=driver.find_element_by_id("nav-recently-viewed")
        Hover = ActionChains(driver).move_to_element(BrowserHistory)
        Hover.perform()
        BrowserHistory.click()

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Browsing History')]")))
        SearchElementPresence=self.isElementPresent("//*[contains(text(), 'Browsing History')]")
        assert SearchElementPresence


    def getValuesfromCSV(self,filepath):
        with open(filepath) as csvDataFile:
            csvReader = csv.DictReader(csvDataFile)
            for row in csvReader:
                username=row['Username']
                password=row['password']
                url=row['Url']
            return username,password,url


    def login(self, id, upassword,url):

         self.driver.get(url)
         self.driver.maximize_window()
         SignIn = self.driver.find_element_by_id("nav-link-accountList")
         SignIn.click()
         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "ap_email")))
         Email = self.driver.find_element_by_name("email")
         Email.send_keys(id)
         password = self.driver.find_element_by_name("password")
         password.send_keys(upassword)
         password.send_keys(Keys.ENTER)
         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "nav-logo")))


    def isElementPresent(self, locator):
        try:
            self.driver.find_element_by_xpath(locator)
        except NoSuchElementException:
            return False
        return True


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

