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

function showNotification(message, type = 'success') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    
    // Add content
    notification.innerHTML = `
        <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
        <span class="notification-message">${message}</span>
        <span class="notification-close">
            <i class="fas fa-times"></i>
        </span>
    `;
    
    // Add to document
    document.body.appendChild(notification);
    
    // Show notification
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    
    // Add close button functionality
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.addEventListener('click', () => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    });
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 5000);
}

// Add event listener to collaboration form
document.addEventListener('DOMContentLoaded', function() {
    const collabForm = document.querySelector('.collab-form');
    if (collabForm) {
        collabForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Simulate form submission
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