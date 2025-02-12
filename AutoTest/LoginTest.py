
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# inherit TestCase Class and create a new test class
username ='ADMIN'
access_key = ''
class DjangoTest(unittest.TestCase):
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
      
  
    # cleanup method called after every test performed
    # TH1 nhap username đ, pw sai  ---> KQ kỳ vọng login f
    # TH2 Nhap username sai, pw đúng --> login f 
    # TH3 nhập đúng cả 2 --> loging thành công ---> vào trong trang hệ thông 
    # khong nhap gi het --- login f 
    def tearDown(self):
        self.driver.close()
    
    def test_unit_login_3(self):
        # try:
        # get driver
        print('bat dau')
        driver = self.driver
        # get python.org using selenium
        driver.get("http://127.0.0.1:8000/login")
        inputUserName  = driver.find_element(By.NAME,value="username")
       
        inputUserName.send_keys("trung")
        #time.sleep(5)

        password  = driver.find_element(By.NAME,value="password")
   
        password.send_keys("123456")
        #time.sleep(5)

        password.send_keys(Keys.RETURN)

        actualTitle = driver.title 
        print(actualTitle)
        # assert actualTitle ,"Trang Bất Động Sản UTH Land"
        assert(actualTitle == "Trang Bất Động Sản UTH Land")
        # assert 2 + 2 == 5, "Houston we've got a problem"

        # receive data
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
    
    def test_unit_login_1(self):
        driver = self.driver

        driver.get("http://127.0.0.1:8000/login")
        inputUserName = driver.find_element(By.NAME, value="username")
        inputUserName.send_keys("trung")
        #time.sleep(5)

        password = driver.find_element(By.NAME, value="password")
        password.send_keys("SSSSSSSSSSS")
        #time.sleep(5)

        password.send_keys(Keys.RETURN)
        #time.sleep(10)

        actualTitle = driver.title 
        print(actualTitle)
        assert(actualTitle == "Login")  
        
    def test_unit_login_2(self):
        driver = self.driver

        driver.get("http://127.0.0.1:8000/login")
        inputUserName = driver.find_element(By.NAME, value="username")
        inputUserName.send_keys("TTTTTTTTTTTT")
        #time.sleep(5)

        password = driver.find_element(By.NAME, value="password")
        password.send_keys("123456")
        #time.sleep(5)

        password.send_keys(Keys.RETURN)
        #time.sleep(10)

        actualTitle = driver.title 
        print(actualTitle)
        assert(actualTitle == "Login")  # Kiểm tra không vào được trang chủ
# execute the script
if __name__ == "__main__":
    unittest.main()