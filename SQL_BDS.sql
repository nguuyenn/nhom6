CREATE DATABASE QuanLyBatDongSan;
USE QuanLyBatDongSan;
CREATE TABLE tinh_thanh (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_tinh_thanh VARCHAR(100) NOT NULL
);
CREATE TABLE du_an (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_du_an VARCHAR(100) NOT NULL,
    mo_ta TEXT,
    tinh_thanh_id INT,
    FOREIGN KEY (tinh_thanh_id) REFERENCES tinh_thanh(id)
);
CREATE TABLE bat_dong_san (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loai VARCHAR(50),
    dia_chi VARCHAR(255),
    gia DECIMAL(15, 2),
    tinh_thanh_id INT,
    du_an_id INT,
    FOREIGN KEY (tinh_thanh_id) REFERENCES tinh_thanh(id),
    FOREIGN KEY (du_an_id) REFERENCES du_an(id)
);
INSERT INTO tinh_thanh (ten_tinh_thanh) VALUES
('Hà Nội'),
('TP Hồ Chí Minh'),
('Đà Nẵng'),
('Hải Phòng'),
('Cần Thơ'),
('An Giang'),
('Bà Rịa - Vũng Tàu'),
('Bắc Giang'),
('Bắc Kạn'),
('Bạc Liêu'),
('Bắc Ninh'),
('Bến Tre'),
('Bình Định'),
('Bình Dương'),
('Bình Phước'),
('Bình Thuận'),
('Cà Mau'),
('Cao Bằng'),
('Đắk Lắk'),
('Đắk Nông'),
('Điện Biên'),
('Đồng Nai'),
('Đồng Tháp'),
('Gia Lai'),
('Hà Giang'),
('Hà Nam'),
('Hà Tĩnh'),
('Hải Dương'),
('Hậu Giang'),
('Hòa Bình'),
('Hưng Yên'),
('Khánh Hòa'),
('Kiên Giang'),
('Kon Tum'),
('Lai Châu'),
('Lâm Đồng'),
('Lạng Sơn'),
('Lào Cai'),
('Long An'),
('Nam Định'),
('Nghệ An'),
('Ninh Bình'),
('Ninh Thuận'),
('Phú Thọ'),
('Quảng Bình'),
('Quảng Nam'),
('Quảng Ngãi'),
('Quảng Ninh'),
('Quảng Trị'),
('Sóc Trăng'),
('Sơn La'),
('Tây Ninh'),
('Thái Bình'),
('Thái Nguyên'),
('Thanh Hóa'),
('Thừa Thiên Huế'),
('Tiền Giang'),
('Trà Vinh'),
('Tuyên Quang'),
('Vĩnh Long'),
('Vĩnh Phúc'),
('Yên Bái');
INSERT INTO tinh_thanh (ten_tinh_thanh)
VALUES ('Phú Yên');

INSERT INTO du_an (ten_du_an, mo_ta, tinh_thanh_id) VALUES
('Nhà số 1', 'Nhà đẹp tại trung tâm thành phố', 2),
('Nhà số 2', 'Đất nền giá rẻ', 14),
('Nhà số 3', 'Căn hộ cao cấp view đẹp', 2),
('Đất nền vị trí đẹp', 'Đất nền vị trí đẹp, gần khu công nghiệp',39),
('Đất nền trung tâm', 'Đất nền trung tâm, tiện xây dựng',22),
('Đất giá rẻ', 'Đất giá rẻ, đầu tư sinh lời', 15);

INSERT INTO bat_dong_san (loai, dia_chi, gia, tinh_thanh_id, du_an_id) VALUES
('Nhà ở', 'Quận 1, TP.HCM', 2000000000, 2, 1),
('Nhà ở', ' Bình Dương', 1200000000, 14, 2),
('Nhà ở', 'Quận 2, TP.HCM', 3500000000, 2, 3),
('Đất', 'Long An', 900000000, 39, 4),
('Đất', 'Biên Hòa, Đồng Nai', 1500000000, 22, 5),
('Đất', 'Bình Phước', 750000000, 15, 6);

