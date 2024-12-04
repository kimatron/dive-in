// Site-wide functionality
document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

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

    // Initialize card animations
    const cards = document.querySelectorAll('.post-card');
    
    if (cards.length > 0) {
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
    }

    // Lazy loading for images
    const lazyImages = document.querySelectorAll('.post-card__image[data-src]');
    
    if (lazyImages.length > 0) {
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

        lazyImages.forEach(img => {
            imageObserver.observe(img);
        });
    }

    // Pagination effects
    const paginationLinks = document.querySelectorAll('.page-link');
    
    if (paginationLinks.length > 0) {
        paginationLinks.forEach(link => {
            // Ripple effect
            link.addEventListener('click', function(e) {
                let x = e.clientX - e.target.offsetLeft;
                let y = e.clientY - e.target.offsetTop;
                
                let ripple = document.createElement('span');
                ripple.className = 'ripple';
                ripple.style.left = x + 'px';
                ripple.style.top = y + 'px';
                
                this.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
            });
            
            // Hover animation
            link.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px)';
            });
            
            link.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
            });
        });
    }

    // Copy Link Functionality
    const copyButton = document.getElementById('copyLink');
    if (copyButton) {
        copyButton.addEventListener('click', function() {
            const url = window.location.href;
            navigator.clipboard.writeText(url)
                .then(() => {
                    copyButton.classList.add('copied');
                    const span = copyButton.querySelector('span');
                    const icon = copyButton.querySelector('i');
                    if (span) span.textContent = 'Copied!';
                    if (icon) icon.className = 'fas fa-check';
                    
                    setTimeout(() => {
                        copyButton.classList.remove('copied');
                        if (span) span.textContent = 'Copy Link';
                        if (icon) icon.className = 'fas fa-link';
                    }, 2000);
                })
                .catch(err => {
                    console.error('Failed to copy:', err);
                });
        });
    }

    // Generate Table of Contents
    const articleContent = document.querySelector('.post-content');
    const tocContent = document.getElementById('toc-content');
    
    if (articleContent && tocContent) {
        const headings = articleContent.querySelectorAll('h2, h3, h4');
        if (headings.length > 0) {
            const toc = document.createElement('ul');
            toc.className = 'toc-list';
            
            headings.forEach((heading, index) => {
                // Add ID to heading if it doesn't have one
                if (!heading.id) {
                    heading.id = `heading-${index}`;
                }
                
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = `#${heading.id}`;
                a.textContent = heading.textContent;
                a.className = `toc-link toc-${heading.tagName.toLowerCase()}`;
                
                li.appendChild(a);
                toc.appendChild(li);

                // Add click event for smooth scrolling
                a.addEventListener('click', function(e) {
                    e.preventDefault();
                    heading.scrollIntoView({ behavior: 'smooth' });
                });
            });

            tocContent.appendChild(toc);

            // Add scroll spy functionality
            window.addEventListener('scroll', () => {
                const fromTop = window.scrollY + 100;

                headings.forEach(heading => {
                    const link = tocContent.querySelector(`a[href="#${heading.id}"]`);
                    if (!link) return;

                    const section = heading.parentElement;
                    const offsetTop = heading.offsetTop;
                    const offsetBottom = offsetTop + section.offsetHeight;

                    if (fromTop >= offsetTop && fromTop <= offsetBottom) {
                        link.classList.add('active');
                    } else {
                        link.classList.remove('active');
                    }
                });
            });
        }
    }
});