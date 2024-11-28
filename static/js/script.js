// General site functionality
document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Initialize animations
    initializeCardAnimations();
    initializePaginationEffects();
});

// Card animations with Intersection Observer
function initializeCardAnimations() {
    const cards = document.querySelectorAll('.post-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1
    });

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        observer.observe(card);
    });

    // Lazy loading for images
    initializeLazyLoading();
}

// Image lazy loading
function initializeLazyLoading() {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });

    document.querySelectorAll('.post-card__image[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Pagination effects
function initializePaginationEffects() {
    const paginationLinks = document.querySelectorAll('.page-link');
    
    paginationLinks.forEach(link => {
        // Add ripple effect
        link.addEventListener('click', handleRippleEffect);
        // Add hover animation
        link.addEventListener('mouseenter', () => link.style.transform = 'translateY(-2px)');
        link.addEventListener('mouseleave', () => link.style.transform = 'translateY(0)');
    });
}

function handleRippleEffect(e) {
    let ripple = document.createElement('span');
    ripple.className = 'ripple';
    ripple.style.left = `${e.clientX - e.target.offsetLeft}px`;
    ripple.style.top = `${e.clientY - e.target.offsetTop}px`;
    
    this.appendChild(ripple);
    setTimeout(() => ripple.remove(), 600);
}