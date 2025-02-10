-- Tạo database
CREATE DATABASE QuanLyBatDongSan;
USE QuanLyBatDongSan;

-- Bảng tỉnh/thành phố
CREATE TABLE tinh_thanh (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_tinh_thanh VARCHAR(100) NOT NULL UNIQUE
);

-- Bảng loại bất động sản
CREATE TABLE loai_bat_dong_san (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_loai VARCHAR(50) NOT NULL UNIQUE
);

-- Bảng dự án
CREATE TABLE du_an (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_du_an VARCHAR(100) NOT NULL,
    mo_ta TEXT,
    tinh_thanh_id INT,
    FOREIGN KEY (tinh_thanh_id) REFERENCES tinh_thanh(id) ON DELETE CASCADE
);

-- Bảng người dùng
CREATE TABLE nguoi_dung (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ho_ten VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    mat_khau VARCHAR(255) NOT NULL,
    so_dien_thoai VARCHAR(15) UNIQUE,
    loai_nguoi_dung ENUM('admin', 'nguoi_mua', 'nguoi_ban') NOT NULL DEFAULT 'nguoi_ban'
);

-- Bảng bất động sản
CREATE TABLE bat_dong_san (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loai_id INT,
    dia_chi VARCHAR(255) NOT NULL,
    gia DECIMAL(18, 2) NOT NULL,
    dien_tich FLOAT NOT NULL CHECK (dien_tich > 0),
    mo_ta TEXT,
    hinh_anh VARCHAR(255),
    ngay_dang TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    trang_thai ENUM('dang_ban', 'da_ban', 'dang_cho_thue', 'da_cho_thue') DEFAULT 'dang_ban',
    tinh_thanh_id INT,
    du_an_id INT,
    nguoi_dang_id INT,
    FOREIGN KEY (loai_id) REFERENCES loai_bat_dong_san(id) ON DELETE CASCADE,
    FOREIGN KEY (tinh_thanh_id) REFERENCES tinh_thanh(id) ON DELETE CASCADE,
    FOREIGN KEY (du_an_id) REFERENCES du_an(id) ON DELETE SET NULL,
    FOREIGN KEY (nguoi_dang_id) REFERENCES nguoi_dung(id) ON DELETE CASCADE
);

-- Bảng giao dịch bất động sản
CREATE TABLE giao_dich (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bat_dong_san_id INT,
    nguoi_mua_id INT,
    gia_giao_dich DECIMAL(18, 2) NOT NULL,
    ngay_giao_dich TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bat_dong_san_id) REFERENCES bat_dong_san(id) ON DELETE CASCADE,
    FOREIGN KEY (nguoi_mua_id) REFERENCES nguoi_dung(id) ON DELETE CASCADE
);

