import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        chromepath = "C:/Users/bhagi/Downloads/chromedriver_win32/chromedriver.exe"
        self.driver = webdriver.Chrome(chromepath)

    def test_search_in_python_org(self):

        result='fail'
        driver = self.driver
        driver.get("https://www.python.org")
        driver.maximize_window()
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elemtext=driver.find_element_by_name("q").text
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        if elemtext=='q':
            result='pass'
        return result




    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

