import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date
import os
import time

class NewBDSTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/batdongsan-new")
        
    def tearDown(self):
        self.driver.close()

    def clear_year_field(self, driver):
        """Hàm xóa năm mặc định"""
        year_field = driver.find_element(By.NAME, "year")
        year_field.send_keys(Keys.CONTROL + "a")  # Chọn toàn bộ text
        year_field.send_keys(Keys.DELETE)  # Xóa text đã chọn
        time.sleep(1)  # Đợi 1 giây sau khi xóa
        
    # Test case 1: Kiểm tra khi nhập đầy đủ thông tin hợp lệ
    def test_submit_valid_bds(self):
        driver = self.driver
        
        driver.find_element(By.NAME, "name").send_keys("Chung cư cao cấp Green Park")
        time.sleep(2)
        
        driver.find_element(By.NAME, "category").send_keys("Nhà")
        time.sleep(2)
        
        driver.find_element(By.NAME, "local_TT").send_keys("TP.HCM")
        time.sleep(2)
        
        driver.find_element(By.NAME, "area").send_keys("75m2")
        time.sleep(2)
        
        self.clear_year_field(driver)
        driver.find_element(By.NAME, "year").send_keys("2024")
        time.sleep(2)
        
        driver.find_element(By.NAME, "startDate").send_keys("02-12-2025")
        time.sleep(2)
        
        
        driver.find_element(By.NAME, "information").send_keys("Căn hộ cao cấp với đầy đủ tiện nghi")
        time.sleep(2)
        
        driver.find_element(By.NAME, "price").send_keys("2.5 tỷ")
        time.sleep(2)
        
    
        driver.find_element(By.NAME, "author").send_keys("Lương Đức Quang Trung")
        time.sleep(2)

        # Upload ảnh
        image_path = os.path.abspath("test_images/sample_property.jpg")
        driver.find_element(By.NAME, "profile_picture").send_keys(image_path)
        time.sleep(2)

        driver.find_element(By.NAME, "author").send_keys(Keys.RETURN)
        time.sleep(2)
        
        actualURL = driver.current_url
        print(f"URL hiện tại: {actualURL}")
        assert "batdongsan/" in actualURL

    # Test case 2: Kiểm tra khi thiếu các trường bắt buộc
    def test_submit_missing_required(self):
        driver = self.driver
        driver.find_element(By.NAME, "name").send_keys("Chung cư cao cấp Green Park")
        time.sleep(2)
        
        driver.find_element(By.NAME, "category").send_keys("Apartment")
        time.sleep(2)
        

        driver.find_element(By.NAME, "area").send_keys("75m2")
        time.sleep(2)
  
        driver.find_element(By.NAME, "information").send_keys("Căn hộ cao cấp với đầy đủ tiện nghi")
        time.sleep(2)
        
        driver.find_element(By.NAME, "price").send_keys("2.5 tỷ")
        time.sleep(2)
        
    
        driver.find_element(By.NAME, "author").send_keys("Lương Đức Quang Trung")
        time.sleep(2)

        # Upload ảnh
        image_path = os.path.abspath("test_images/sample_property.jpg")
        driver.find_element(By.NAME, "profile_picture").send_keys(image_path)
        time.sleep(2)

        driver.find_element(By.NAME, "author").send_keys(Keys.RETURN)
        time.sleep(2)
        
        actualURL = driver.current_url
        print(f"URL hiện tại: {actualURL}")
        assert "batdongsan-new" in actualURL

    # Test case 3: Kiểm tra với năm không hợp lệ
    def test_invalid_year(self):
        driver = self.driver
        
        driver.find_element(By.NAME, "name").send_keys("Căn hộ test")
        time.sleep(2)
        self.clear_year_field(driver)
        driver.find_element(By.NAME, "year").send_keys("20000")  # Năm không hợp lệ
        time.sleep(2)
        
        driver.find_element(By.NAME, "startDate").send_keys("02-12-2025")
        time.sleep(2)
        
        driver.find_element(By.NAME, "year").send_keys(Keys.RETURN)
        time.sleep(2)
        
        actualURL = driver.current_url
        print(f"URL hiện tại: {actualURL}")
        assert "batdongsan-new" in actualURL

    # Test case 4: Kiểm tra với độ dài vượt quá giới hạn
    def test_oversized_fields(self):
        driver = self.driver
        
        driver.find_element(By.NAME, "name").send_keys("A" * 151)  # Vượt quá max_length
        time.sleep(2)
        
        driver.find_element(By.NAME, "category").send_keys("A" * 11)  # Vượt quá max_length
        time.sleep(2)
        self.clear_year_field(driver)
        driver.find_element(By.NAME, "year").send_keys("2024")
        time.sleep(2)
        
        driver.find_element(By.NAME, "startDate").send_keys("2024-02-15")
        time.sleep(2)
        
        driver.find_element(By.NAME, "name").send_keys(Keys.RETURN)
        time.sleep(2)
        
        actualURL = driver.current_url
        print(f"URL hiện tại: {actualURL}")
        assert "batdongsan-new" in actualURL  # kiem tra xem url hien tai co giong voi url mong muon chua

    # Test case 5: Kiểm tra với định dạng ngày không hợp lệ
    def test_invalid_date(self):
        driver = self.driver
        
        driver.find_element(By.NAME, "name").send_keys("Căn hộ test")
        time.sleep(2)
        self.clear_year_field(driver)
        driver.find_element(By.NAME, "year").send_keys("2024")
        time.sleep(2)
        
        driver.find_element(By.NAME, "startDate").send_keys("ngày-không-hợp-lệ")
        time.sleep(2)
        
        driver.find_element(By.NAME, "startDate").send_keys(Keys.RETURN)
        time.sleep(2)
        
        actualURL = driver.current_url
        print(f"URL hiện tại: {actualURL}")
        assert "batdongsan-new" in actualURL

    # Test case 6: Kiểm tra với file ảnh không hợp lệ
    def test_invalid_image(self):
        driver = self.driver
        
        driver.find_element(By.NAME, "name").send_keys("Căn hộ test")
        time.sleep(2)
        self.clear_year_field(driver)
        driver.find_element(By.NAME, "year").send_keys("2024")
        time.sleep(2)
        
        driver.find_element(By.NAME, "startDate").send_keys("2024-02-15")
        time.sleep(2)
        
        # Upload file không hợp lệ
        invalid_file_path = os.path.abspath("test_files/invalid.txt")
        driver.find_element(By.NAME, "profile_picture").send_keys(invalid_file_path)
        time.sleep(2)
        
        driver.find_element(By.NAME, "name").send_keys(Keys.RETURN)
        time.sleep(2)
        
        actualURL = driver.current_url
        print(f"URL hiện tại: {actualURL}")
        assert "batdongsan-new" in actualURL

if __name__ == "__main__":
    unittest.main()