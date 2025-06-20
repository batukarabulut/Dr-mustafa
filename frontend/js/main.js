// ===== CONTACT FORM HANDLER =====
document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = new FormData(form);
    const alertDiv = document.getElementById('contact-alert');
    const submitBtn = form.querySelector('button[type="submit"]');
    const btnText = submitBtn.querySelector('.btn-text');
    const btnSpinner = submitBtn.querySelector('.btn-spinner');
    
    // Show loading state
    btnText.textContent = 'Gönderiliyor...';
    btnSpinner.classList.remove('d-none');
    submitBtn.disabled = true;
    
    try {
        const response = await fetch('http://127.0.0.1:8000/api/contact/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: formData.get('name'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                subject: formData.get('subject'),
                message: formData.get('message')
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            alertDiv.className = 'alert alert-success';
            alertDiv.textContent = 'Mesajınız başarıyla gönderildi! En kısa sürede size dönüş yapacağız.';
            form.reset();
        } else {
            alertDiv.className = 'alert alert-danger';
            alertDiv.textContent = 'Bir hata oluştu. Lütfen tekrar deneyin.';
        }
    } catch (error) {
        alertDiv.className = 'alert alert-danger';
        alertDiv.textContent = 'Bağlantı hatası. Lütfen internet bağlantınızı kontrol edin.';
    }
    
    // Reset button state
    btnText.textContent = 'Mesaj Gönder';
    btnSpinner.classList.add('d-none');
    submitBtn.disabled = false;
    alertDiv.classList.remove('d-none');
    
    // Hide alert after 5 seconds
    setTimeout(() => {
        alertDiv.classList.add('d-none');
    }, 5000);
});

// ===== MOBILE MENU TOGGLE =====
document.addEventListener('DOMContentLoaded', function() {
    console.log('Website loaded successfully!');
});