import unittest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TrackYourOrderPackage(unittest.TestCase):

    def setUp(self):
        chromepath = "C:/Users/bhagi/Downloads/chromedriver_win32/chromedriver.exe"
        #options=webdriver.ChromeOptions()
        #options.add_argument('headless')
        self.driver = webdriver.Chrome(chromepath)

    def test_Track_your_order_package(self):

        driver = self.driver
        id, password, url =self.getValuesfromCSV('C:\\Users\\bhagi\\PycharmProjects\\APIFuzzer\propertyFile.csv')
        self.login(id,password,url)
        OrdersInHome=driver.find_element_by_xpath("//span[text()='Orders']")
        OrdersInHome.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "a-autoid-0-announce")))

        ParticulaOrder=driver.find_element_by_xpath("//a[contains(text(),'Cryptography')]")
        driver.execute_script("arguments[0].scrollIntoView();", ParticulaOrder)

        trackpackage=driver.find_element_by_id("a-autoid-47-announce")
        driver.execute_script("arguments[0].scrollIntoView();", trackpackage)
        trackpackage.click()
        SearchElementPresence=self.isElementPresent("//span[contains(text(),'Track Package')]")
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

