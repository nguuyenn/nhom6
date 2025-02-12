document.addEventListener('DOMContentLoaded', function() {
    const userInfo = document.querySelector('.user-info');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    
    // Ensure dropdown is hidden on page load
    if (dropdownMenu) {
        dropdownMenu.style.display = 'none';
    }
    
    // Toggle dropdown when clicking on user info
    if (userInfo) {
        userInfo.addEventListener('click', function(event) {
            event.stopPropagation();
            dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
        });
    }
    
    // Close dropdown when clicking outside
    document.addEventListener('click', function(event) {
        if (dropdownMenu && !userInfo.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
    });
});