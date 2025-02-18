document.addEventListener('DOMContentLoaded', function() {
    const userInfo = document.querySelector('.user-info');
    const dropdownMenu = document.getElementById('user-dropdown');
    
    // Toggle dropdown when clicking on user info
    if (userInfo) {
        userInfo.addEventListener('click', function(e) {
            e.stopPropagation();
            dropdownMenu.classList.toggle('show');
        });
    }
    
    // Close dropdown when clicking outside
    document.addEventListener('click', function(e) {
        if (!userInfo?.contains(e.target) && dropdownMenu?.classList.contains('show')) {
            dropdownMenu.classList.remove('show');
        }
    });
});