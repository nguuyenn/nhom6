<?php  
session_start();  

// Giả sử thông tin admin là tĩnh  
$adminUsername = "admin";  
$adminPassword = "123456";  

// Lấy thông tin người dùng nhập  
$username = $_POST['username'];  
$password = $_POST['password'];  

// Kiểm tra thông tin  
if ($username === $adminUsername && $password === $adminPassword) {  
    $_SESSION['isAdmin'] = true; // Gán giá trị xác định admin đã đăng nhập  
    header("Location: admin.html"); // Chuyển hướng đến admin.html  
    exit;  
} else {  
    $_SESSION['login_error'] = "Sai tên người dùng hoặc mật khẩu.";  
    header("Location: login.html"); // Quay lại trang đăng nhập  
    exit;  
}  
?>