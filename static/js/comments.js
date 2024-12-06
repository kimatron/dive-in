document.addEventListener('DOMContentLoaded', () => {
    // Get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    const postSlugElement = document.getElementById('postSlug');
    if (!postSlugElement) return;
    const postSlug = postSlugElement.getAttribute('data-slug');

    // Initialize the modals
    const editModal = new bootstrap.Modal(document.getElementById('editModal'));
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));

    let currentCommentId = null;

    // Handle edit and delete buttons
    const commentsList = document.querySelector('.comments-list');
    if (commentsList) {
        commentsList.addEventListener('click', (e) => {
            if (e.target.closest('.btn-edit')) {
                const editButton = e.target.closest('.btn-edit');
                currentCommentId = editButton.getAttribute('comment_id');
                const commentElement = document.querySelector(`#comment${currentCommentId}`);
                const commentText = commentElement.textContent.trim();
                document.getElementById('editCommentText').value = commentText;
                editModal.show();
            }
            
            if (e.target.closest('.btn-delete')) {
                const deleteButton = e.target.closest('.btn-delete');
                currentCommentId = deleteButton.getAttribute('comment_id');
                deleteModal.show();
            }
        });
    }

    // Handle edit form submission
    const saveEditButton = document.getElementById('saveEdit');
    if (saveEditButton) {
        saveEditButton.addEventListener('click', async () => {
            if (!currentCommentId) return;
            
            const updatedText = document.getElementById('editCommentText').value;
            try {
                const response = await fetch(`/post/${postSlug}/comment_edit/${currentCommentId}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': csrftoken,
                    },
                    body: `body=${encodeURIComponent(updatedText)}`
                });

                if (response.ok) {
                    const commentElement = document.querySelector(`#comment${currentCommentId}`);
                    commentElement.innerHTML = updatedText;

                    const commentCard = commentElement.closest('.comment-card');
                    if (!commentCard.querySelector('.pending-notice')) {
                        const pendingNotice = document.createElement('div');
                        pendingNotice.className = 'pending-notice';
                        pendingNotice.innerHTML = `
                            <i class="fas fa-clock"></i>
                            Your edited comment is awaiting approval
                        `;
                        commentCard.appendChild(pendingNotice);
                    }

                    showToast('Comment updated successfully and awaiting approval', 'success');
                    editModal.hide();
                } else {
                    throw new Error('Failed to update comment');
                }
            } catch (error) {
                console.error('Error:', error);
                showToast('Error updating comment. Please try again.', 'error');
            }
        });
    }

    // Handle delete confirmation
    const deleteConfirmButton = document.getElementById('deleteConfirm');
    if (deleteConfirmButton) {
        deleteConfirmButton.addEventListener('click', async (e) => {
            e.preventDefault();
            if (!currentCommentId) return;

            try {
                const response = await fetch(`/post/${postSlug}/comment_delete/${currentCommentId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrftoken,
                    }
                });

                if (response.ok) {
                    const commentCard = document.querySelector(`#comment${currentCommentId}`).closest('.comment-card');
                    commentCard.remove();
                    showToast('Comment deleted successfully', 'success');
                    deleteModal.hide();
                } else {
                    throw new Error('Failed to delete comment');
                }
            } catch (error) {
                console.error('Error:', error);
                showToast('Error deleting comment. Please try again.', 'error');
            }
        });
    }

    // Function to show toast notifications
    function showToast(message, type) {
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white border-0 bg-${type}`;
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');
        
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'} me-2"></i>
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        `;

        const toastContainer = document.querySelector('.toast-container');
        if (toastContainer) {
            toastContainer.appendChild(toast);
            const bsToast = new bootstrap.Toast(toast, { autohide: true, delay: 3000 });
            bsToast.show();

            toast.addEventListener('hidden.bs.toast', () => {
                toast.remove();
            });
        }
    }

    // Initialize any existing Django messages as Bootstrap toasts
    document.querySelectorAll('.toast').forEach(toastElement => {
        const toast = new bootstrap.Toast(toastElement, { autohide: true, delay: 3000 });
        toast.show();
    });
});