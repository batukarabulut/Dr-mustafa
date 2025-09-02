// ===== CONTACT FORM HANDLER =====
document.getElementById('contactForm')?.addEventListener('submit', async function(e) {
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
    // Collapse navbar when a leaf nav-link is clicked (but NOT dropdown toggles)
    document.querySelectorAll('.navbar .nav-link').forEach((link) => {
        link.addEventListener('click', (ev) => {
            const isDropdownToggle = link.classList.contains('dropdown-toggle') || link.getAttribute('data-bs-toggle') === 'dropdown';
            if (isDropdownToggle) {
                // keep navbar open while toggling dropdown
                ev.preventDefault();
                ev.stopPropagation();
                // toggle related menu for mobile
                if (window.innerWidth < 992) {
                    const menu = link.nextElementSibling;
                    if (menu && menu.classList.contains('dropdown-menu')) {
                        const shown = menu.classList.contains('show');
                        document.querySelectorAll('.navbar .dropdown-menu.show').forEach(m => m.classList.remove('show'));
                        if (!shown) menu.classList.add('show');
                    }
                }
                return;
            }
            const navbarCollapse = document.querySelector('.navbar .collapse.show');
            if (navbarCollapse) {
                const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse) || new bootstrap.Collapse(navbarCollapse, { toggle: false });
                bsCollapse.hide();
            }
        });
    });

    // Allow dropdowns to toggle properly on mobile via click (do not close parent collapse)
    document.querySelectorAll('.navbar .dropdown-toggle').forEach((toggle) => {
        toggle.addEventListener('click', function (e) {
            if (window.innerWidth < 992) {
                e.preventDefault();
                e.stopPropagation();
                const menu = this.nextElementSibling;
                if (menu && menu.classList.contains('dropdown-menu')) {
                    const isShown = menu.classList.contains('show');
                    document.querySelectorAll('.navbar .dropdown-menu.show').forEach(m => {
                        if (m !== menu) m.classList.remove('show');
                    });
                    if (!isShown) menu.classList.add('show');
                }
            }
        });
    });

    document.addEventListener('click', function(e) {
        if (window.innerWidth < 992) {
            if (!e.target.closest('.navbar .dropdown')) {
                document.querySelectorAll('.navbar .dropdown-menu.show').forEach(m => m.classList.remove('show'));
            }
        }
    });
    // Add reveal classes automatically to common elements across pages
    const addRevealDefaults = () => {
        const defaultRevealSelectors = [
            '.section-title',
            '.card',
            '.service-image-card',
            '.team-card',
            '.contact-card',
            '.accordion-item',
            '.feature-box',
            '.process-number',
            '.service-content',
            '.review-card'
        ];
        const defaultRevealUpSelectors = [
            '.row.text-center > [class*="col-"]',
            '.row .col-lg-3.mb-4',
            '.row .col-md-6.mb-4'
        ];

        defaultRevealSelectors.forEach(sel => {
            document.querySelectorAll(sel).forEach(el => {
                if (!el.classList.contains('reveal') &&
                    !el.classList.contains('reveal-up') &&
                    !el.classList.contains('reveal-down') &&
                    !el.classList.contains('reveal-left') &&
                    !el.classList.contains('reveal-right')) {
                    el.classList.add('reveal');
                }
            });
        });

        defaultRevealUpSelectors.forEach(sel => {
            document.querySelectorAll(sel).forEach(el => {
                if (!el.classList.contains('reveal') &&
                    !el.classList.contains('reveal-up') &&
                    !el.classList.contains('reveal-down') &&
                    !el.classList.contains('reveal-left') &&
                    !el.classList.contains('reveal-right')) {
                    el.classList.add('reveal-up');
                }
            });
        });
    };

    addRevealDefaults();

    // Scroll reveal (IntersectionObserver)
    const revealElements = document.querySelectorAll('.reveal, .reveal-up, .reveal-down, .reveal-left, .reveal-right');
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('reveal-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { root: null, rootMargin: '0px 0px -10% 0px', threshold: 0.15 });

        revealElements.forEach(el => observer.observe(el));
    } else {
        // Fallback: show all
        revealElements.forEach(el => el.classList.add('reveal-visible'));
    }

    // Count-up animation for numbers
    const counters = document.querySelectorAll('.count-up');
    const runCounter = (el) => {
        if (el.dataset.started === '1') return;
        el.dataset.started = '1';
        const target = parseFloat(el.getAttribute('data-count')) || 0;
        const duration = parseInt(el.getAttribute('data-duration') || '1200', 10);
        const decimals = parseInt(el.getAttribute('data-decimals') || '0', 10);
        const suffix = el.getAttribute('data-suffix') || '';
        const start = performance.now();

        const step = (now) => {
            const progress = Math.min((now - start) / duration, 1);
            const value = (target * progress).toFixed(decimals);
            el.textContent = value + suffix;
            if (progress < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
    };

    const isInViewport = (el) => {
        const rect = el.getBoundingClientRect();
        return (
            rect.top < (window.innerHeight || document.documentElement.clientHeight) &&
            rect.bottom > 0 &&
            rect.left < (window.innerWidth || document.documentElement.clientWidth) &&
            rect.right > 0
        );
    };

    // Kick off immediately for any counters already visible
    counters.forEach((c) => { if (isInViewport(c)) runCounter(c); });

    if ('IntersectionObserver' in window) {
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    runCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        counters.forEach(c => counterObserver.observe(c));
    } else {
        // Fallback: listen to scroll and try to start when visible
        const onScrollCheck = () => {
            counters.forEach((c) => { if (isInViewport(c)) runCounter(c); });
        };
        onScrollCheck();
        window.addEventListener('scroll', onScrollCheck, { passive: true });
    }

    // Back to top button
    const backToTop = document.createElement('button');
    backToTop.className = 'back-to-top';
    backToTop.setAttribute('aria-label', 'Yukarı dön');
    backToTop.innerHTML = '<i class="fas fa-chevron-up"></i>';
    document.body.appendChild(backToTop);

    const toggleBackToTop = () => {
        if (window.scrollY > 300) backToTop.classList.add('visible');
        else backToTop.classList.remove('visible');
    };
    window.addEventListener('scroll', toggleBackToTop, { passive: true });
    toggleBackToTop();

    backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // WhatsApp floating button (left bottom)
    const wa = document.createElement('a');
    wa.href = 'https://wa.me/905407404077';
    wa.target = '_blank';
    wa.rel = 'noopener';
    wa.className = 'whatsapp-float';
    wa.setAttribute('aria-label', 'WhatsApp ile yazın');
    wa.innerHTML = '<i class="fab fa-whatsapp" style="font-size: 24px;"></i>';
    document.body.appendChild(wa);

    // (Reverted) Keep original hero ordering – removed mobile reordering logic
});