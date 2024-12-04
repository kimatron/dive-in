document.addEventListener('DOMContentLoaded', function() {
    // Stats Animation
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                animateCount(entry.target.querySelector('.stat-number'));
            }
        });
    }, {
        threshold: 0.5
    });

    // Observe stat cards
    document.querySelectorAll('.stat-card').forEach(card => {
        statsObserver.observe(card);
    });

    // Collaboration Form Handler
    const collabForm = document.querySelector('.collab-form');
    if (collabForm) {
        collabForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            fetch(this.action, {
                method: 'POST',
                body: new FormData(this)
            })
            .then(response => {
                if (response.ok) {
                    showNotification('Your collaboration request has been submitted successfully! We\'ll be in touch soon.', 'success');
                    this.reset();
                } else {
                    showNotification('There was an error submitting your request. Please try again.', 'error');
                }
            })
            .catch(() => {
                showNotification('There was an error submitting your request. Please try again.', 'error');
            });
        });
    }
});

function animateCount(element) {
    const target = parseInt(element.dataset.target);
    const duration = 2000;
    const step = target / 100;
    const stepTime = duration / 100;
    let current = 0;

    const timer = setInterval(() => {
        current += step;
        element.textContent = Math.round(current);

        if (current >= target) {
            element.textContent = target;
            clearInterval(timer);
        }
    }, stepTime);
}

window.addEventListener('scroll', function() {
    const scrollToTopBtn = document.querySelector('.scroll-to-top');
    if (window.pageYOffset > 300) {
        scrollToTopBtn.classList.add('show');
    } else {
        scrollToTopBtn.classList.remove('show');
    }
});