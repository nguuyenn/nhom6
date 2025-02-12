// Lắng nghe sự kiện khi người dùng nhấn nút "Cập Nhật"
document.getElementById("update-button").addEventListener("click", function () {
  const name = document.getElementById("name").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const address = document.getElementById("address").value.trim();
  const email = document.getElementById("email").value.trim();

  if (!name || !phone || !address || !email) {
    alert("Vui lòng nhập đầy đủ thông tin!");
    return;
  }

  document.getElementById("display-name").textContent = `Họ và Tên: ${name}`;
  document.getElementById(
    "display-phone"
  ).textContent = `Số Điện Thoại: ${phone}`;
  document.getElementById(
    "display-address"
  ).textContent = `Địa Chỉ: ${address}`;
  document.getElementById("display-email").textContent = `Gmail: ${email}`;

  alert("Cập nhật thông tin thành công!");
});

// Xử lý sự kiện tải ảnh đại diện
document.getElementById("upload-button").addEventListener("click", function () {
  document.getElementById("upload-avatar").click();
});

document
  .getElementById("upload-avatar")
  .addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        document.getElementById("avatar").src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  });
