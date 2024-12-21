<?php
session_start();
session_destroy(); // Xóa phiên đăng nhập
header("Location: login.html"); // Quay lại trang login
exit;
?>
