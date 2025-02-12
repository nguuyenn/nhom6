// Lấy các phần tử cần thiết
const chatBtn = document.getElementById("chat-btn");
const chatBox = document.getElementById("chat-box");
const closeChat = document.getElementById("close-chat");
const sendBtn = document.getElementById("send-btn");
const messageInput = document.getElementById("message-input");
const chatContent = document.querySelector(".chat-content");

// Hàm để định dạng ngày giờ
function getCurrentTime() {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, "0");
  const minutes = String(now.getMinutes()).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  const month = String(now.getMonth() + 1).padStart(2, "0"); // Tháng bắt đầu từ 0
  const year = now.getFullYear();

  return `${hours}:${minutes}, ${day}/${month}/${year}`;
}

// Mở hộp nhắn tin khi nhấn vào nút chat
chatBtn.addEventListener("click", () => {
  chatBox.style.display = "flex";
});

// Đóng hộp nhắn tin
closeChat.addEventListener("click", () => {
  chatBox.style.display = "none";
});

// Gửi tin nhắn
sendBtn.addEventListener("click", () => {
  const message = messageInput.value.trim();
  if (message !== "") {
    // Tạo phần tử tin nhắn người dùng
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("chat-message");
    messageDiv.classList.add("sender");
    messageDiv.innerHTML = `
      <div class="message-text">${message}</div>
      <div class="message-time">${getCurrentTime()}</div>
    `;

    // Thêm tin nhắn vào giao diện
    chatContent.appendChild(messageDiv);

    // Cuộn xuống cuối hộp thư
    chatContent.scrollTop = chatContent.scrollHeight;

    // Xóa ô nhập sau khi gửi
    messageInput.value = "";
  }
});
