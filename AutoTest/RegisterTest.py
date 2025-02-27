
import unittest
from selenium import webdriver #Cung cấp các driver để thao tác được với các trình duyệt web
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DjangoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/register")
        
    def tearDown(self):
        self.driver.close()
    #Test case đăng ký thành công khi nhập đầy đủ thông tin hợp lệ
    def test_unit_dang_ky1(self):

        driver = self.driver
        
        driver.find_element(By.NAME, "username").send_keys("trung98621")
        #time.sleep(5)

        driver.find_element(By.NAME, "first_name").send_keys("Luong")
        #time.sleep(5)
        
        driver.find_element(By.NAME, "last_name").send_keys("Trung")
        #time.sleep(5)

        driver.find_element(By.NAME, "email").send_keys("trungdepzai123321@gmail.com")
        #time.sleep(5)

        driver.find_element(By.NAME, "password1").send_keys("123456") 
        #time.sleep(5)

        driver.find_element(By.NAME, "password2").send_keys("123456") 
        #time.sleep(5)

        driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)        
        #time.sleep(5)

        actualTitle = driver.title
        actualURL = driver.current_url
        print(f"Tiêu đề trang hiện tại: {actualTitle}")
        print(f"URL trang hiện tại: {actualURL}")
        assert(actualTitle == "Login")
    
    #Test case khi không nhập bất kỳ thông tin nào     
    # def test_unit_dang_ky2(self):
       
    #     driver = self.driver
        
    #     driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
        
    #     actualTitle = driver.title
    #     assert(actualTitle == "UTHLand Sign Up")        

    # #Test case khi nhập first_name vượt quá độ dài cho phép 
    # def test_unit_dang_ky3(self):

    #     driver = self.driver
        
    #     # Tạo first_name dài hơn 30 ký tự
    #     long_first_name = "A" * 35
        
    #     driver.find_element(By.NAME, "username").send_keys("nguoidung1")
    #     driver.find_element(By.NAME, "first_name").send_keys(long_first_name)
    #     driver.find_element(By.NAME, "last_name").send_keys("Văn A")
    #     driver.find_element(By.NAME, "email").send_keys("nguyenvana@example.com")
    #     driver.find_element(By.NAME, "password1").send_keys("MatKhau123!")
    #     driver.find_element(By.NAME, "password2").send_keys("MatKhau123!")
        
    #     driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
    #     actualTitle = driver.title        
    #     assert(actualTitle == "UTHLand Sign Up")  # Kiểm tra URL không thay đổi
    
    # #Test case khi nhập last_name vượt quá độ dài cho phép 
    # def test_unit_dang_ky4(self):

    #     driver = self.driver
        
    #     # Tạo first_name dài hơn 30 ký tự
    #     long_last_name = "A" * 35
        
    #     driver.find_element(By.NAME, "username").send_keys(long_last_name)
    #     driver.find_element(By.NAME, "first_name").send_keys("Trung")
    #     driver.find_element(By.NAME, "last_name").send_keys("Văn A")
    #     driver.find_element(By.NAME, "email").send_keys("nguyenvana@example.com")
    #     driver.find_element(By.NAME, "password1").send_keys("MatKhau123!")
    #     driver.find_element(By.NAME, "password2").send_keys("MatKhau123!")
        
    #     driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
    #     actualTitle = driver.title
    #     assert(actualTitle == "UTHLand Sign Up")  # Kiểm tra URL không thay đổi
    
    
  
    # #Test case khi nhập email sai định dạng    
    # def test_unit_dang_ky5(self):
        
    #     driver = self.driver
        
    #     driver.find_element(By.NAME, "username").send_keys("nguoidung1")
    #     driver.find_element(By.NAME, "first_name").send_keys("Nguyễn")
    #     driver.find_element(By.NAME, "last_name").send_keys("Văn A")
    #     driver.find_element(By.NAME, "email").send_keys("emailkhonghople")  # Email sai định dạng
    #     driver.find_element(By.NAME, "password1").send_keys("MatKhau123!")
    #     driver.find_element(By.NAME, "password2").send_keys("MatKhau123!")
        
    #     driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
    #     actualTitle = driver.title        
    #     assert(actualTitle == "UTHLand Sign Up")  # Kiểm tra URL không thay đổi
    # #Test case khi bỏ trống trường first_name và last_name 
    # def test_unit_dang_ky6(self):
    #     driver = self.driver
        
        
    #     driver.find_element(By.NAME, "username").send_keys("nguoidung1")
    #     driver.find_element(By.NAME, "email").send_keys("nguyenvana@example.com")
    #     driver.find_element(By.NAME, "password1").send_keys("MatKhau123!")
    #     driver.find_element(By.NAME, "password2").send_keys("MatKhau123!")
        
    #     driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
    #     actualTitle = driver.title        
    #     assert(actualTitle == "UTHLand Sign Up")  # Kiểm tra URL không thay đổi
    
    # #Test case kiểm tra khi 2 mật khẩu không giống nhau
    
    # def test_unit_dang_ky7(self):
    #         driver = self.driver
            
    #         driver.find_element(By.NAME, "username").send_keys("nguoidung1")
    #         driver.find_element(By.NAME, "first_name").send_keys("Nguyễn")
    #         driver.find_element(By.NAME, "last_name").send_keys("Văn A")
    #         driver.find_element(By.NAME, "email").send_keys("nguyenvana@example.com")
    #         driver.find_element(By.NAME, "password1").send_keys("MatKhau123!")
    #         driver.find_element(By.NAME, "password2").send_keys("KhacNhau123!")
            
    #         driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
            
    #         actualTitle = driver.title        
    #         assert(actualTitle == "UTHLand Sign Up") 
            
    #     #Test case kiểm tra khi username vượt quá ký tự cho phép 15 ký tự
    # def test_unit_dang_ky8(self):
    #         driver = self.driver
    #         long_username = "A" * 17
    #         driver.find_element(By.NAME, "username").send_keys(long_username)
    #         driver.find_element(By.NAME, "first_name").send_keys("Nguyễn")
    #         driver.find_element(By.NAME, "last_name").send_keys("Văn A")
    #         driver.find_element(By.NAME, "email").send_keys("nguyenvana@example.com")
    #         driver.find_element(By.NAME, "password1").send_keys("MatKhau123!")
    #         driver.find_element(By.NAME, "password2").send_keys("KhacNhau123!")
            
    #         driver.find_element(By.NAME, "username").send_keys(Keys.RETURN)
            
    #         actualTitle = driver.title        
    #         assert(actualTitle == "UTHLand Sign Up")         

    #     #Testcase khi username quá ngắn
    # def test_unit_dang_ky9(self):
    #         driver = self.driver
    #         driver.find_element(By.NAME, "username").send_keys("aa") # User default ngắn nhất là 3 
    #         driver.find_element(By.NAME, "first_name").send_keys("Nguyễn")
    #         driver.find_element(By.NAME, "last_name").send_keys("Văn A")
    #         driver.find_element(By.NAME, "email").send_keys("nguyenvana@example.com")
    #         driver.find_element(By.NAME, "password1").send_keys("MatKhau123!")
    #         driver.find_element(By.NAME, "password2").send_keys("KhacNhau123!")
            
    #         driver.find_element(By.NAME, "username").send_keys(Keys.RETURN)
            
    #         actualTitle = driver.title        
    #         assert(actualTitle == "UTHLand Sign Up")         


if __name__ == "__main__":
    unittest.main()