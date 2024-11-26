document.addEventListener('DOMContentLoaded', function() {
    // Intersection Observer for stats animation
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

    // Observe all stat cards
    document.querySelectorAll('.stat-card').forEach(card => {
        statsObserver.observe(card);
    });
});

function animateCount(element) {
    const target = parseInt(element.dataset.target);
    const duration = 2000; // Animation duration in milliseconds
    const step = target / 100; // Divide animation into 100 steps
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