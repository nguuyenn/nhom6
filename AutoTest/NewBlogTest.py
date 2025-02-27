import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date
import os
import time

class NewBlogTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/blog-new")
    def tearDown(self):
        self.driver.close()    
    
    
    # Test case 1 khi thong tin day du
    def test_unit_new_blog_1(self):
        driver = self.driver
        
        driver.find_element(By.NAME, "title").send_keys("Day la title test ")
        time.sleep(1)
        
        driver.find_element(By.NAME, "information").send_keys("HELLO HEHE HAHA HUHU HIHI")
        time.sleep(1)
        
        image_path = os.path.abspath("test_images/sample_property.jpg")
        driver.find_element(By.NAME, "profile_picture").send_keys(image_path)
        time.sleep(1)
        
        # Click nút Đăng tin
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        print(f"Submit button text: {submit_button.text}")
        submit_button.click()
        
        actualURL = driver.current_url
        print(f"URL hiện tại: {actualURL}")
        assert "blog" in actualURL
        
        
    # Test case 2: Kiểm tra khi nhập thiếu trường thông tin 
    
    def test_unit_new_blog_2(self):
        driver = self.driver
        
        driver.find_element(By.NAME, "title").send_keys("Day la title test ")
        time.sleep(1)
        

        image_path = os.path.abspath("test_images/sample_property.jpg")
        driver.find_element(By.NAME, "profile_picture").send_keys(image_path)
        time.sleep(1)
        
        # Click nút Đăng tin
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        print(f"Submit button text: {submit_button.text}")
        submit_button.click()
        
        actualURL = driver.current_url
        print(f"URL hiện tại: {actualURL}")
        assert "blog" in actualURL
        
    
if __name__ == "__main__":
    unittest.main()