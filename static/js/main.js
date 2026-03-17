// ===== CONTACT FORM HANDLER (AJAX, same-origin: no CORS) =====
document.getElementById('contact-form')?.addEventListener('submit', async function(e) {
    e.preventDefault();
    var form = e.target;
    var formData = new FormData(form);
    var alertEl = document.getElementById('contact-alert');
    var submitBtn = form.querySelector('button[type="submit"]');
    var btnText = submitBtn ? submitBtn.querySelector('.btn-text') : null;
    var btnSpinner = submitBtn ? submitBtn.querySelector('.btn-spinner') : null;
    var csrfInput = form.querySelector('input[name="csrfmiddlewaretoken"]');

    if (btnText) btnText.textContent = 'Gönderiliyor...';
    if (btnSpinner) btnSpinner.classList.remove('d-none');
    if (submitBtn) submitBtn.disabled = true;

    try {
        var response = await fetch('/api/contact/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfInput ? csrfInput.value : ''
            },
            body: JSON.stringify({
                name: formData.get('name'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                subject: formData.get('subject'),
                message: formData.get('message'),
                kvkk: formData.get('kvkk') === 'on'
            })
        });
        var data = await response.json();

        if (response.ok) {
            if (alertEl) {
                alertEl.className = 'alert alert-success contact-alert-notice';
                alertEl.textContent = 'Mesajınız başarıyla iletildi. En kısa sürede size dönüş yapacağız.';
                alertEl.classList.remove('d-none');
                alertEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
            form.reset();
        } else {
            if (alertEl) {
                alertEl.className = 'alert alert-danger contact-alert-notice';
                alertEl.textContent = data.errors ? Object.values(data.errors).flat().join(' ') : 'Bir hata oluştu. Lütfen tekrar deneyin.';
                alertEl.classList.remove('d-none');
                alertEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }
    } catch (err) {
        if (alertEl) {
            alertEl.className = 'alert alert-danger contact-alert-notice';
            alertEl.textContent = 'Bağlantı hatası. Lütfen tekrar deneyin.';
            alertEl.classList.remove('d-none');
            alertEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    if (btnText) btnText.textContent = 'Mesaj Gönder';
    if (btnSpinner) btnSpinner.classList.add('d-none');
    if (submitBtn) submitBtn.disabled = false;
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