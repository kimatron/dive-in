document.addEventListener('DOMContentLoaded', () => {
    // Initialize Elements
    const editButtons = document.getElementsByClassName("btn-edit");
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteConfirm = document.getElementById("deleteConfirm");
    const editModal = new bootstrap.Modal(document.getElementById("editModal"));

    // Initialize Toasts
    const toastElList = document.querySelectorAll('.toast');
    if (toastElList.length > 0) {
        toastElList.forEach(toast => {
            const bsToast = new bootstrap.Toast(toast, {
                autohide: true,
                delay: 3000
            });
            bsToast.show();
        });
    }

    // Handle Edit and Delete functionality
    const postSlugElement = document.getElementById("postSlug");
    if (postSlugElement) {
        const postSlug = postSlugElement.getAttribute("data-slug");

        // Edit button handlers
        Array.from(editButtons).forEach(button => {
            button.addEventListener("click", function(e) {
                const commentId = this.getAttribute("comment_id");
                const commentContent = document.getElementById(`comment${commentId}`).innerText;
                document.getElementById('editCommentText').value = commentContent.trim();
                editModal.show();

                // Set up save edit button
                document.getElementById('saveEdit').addEventListener('click', function() {
                    const editForm = document.createElement('form');
                    editForm.method = 'POST';
                    editForm.action = `/post/${postSlug}/comment_edit/${commentId}/`;

                    // Add CSRF token
                    const csrfInput = document.createElement('input');
                    csrfInput.type = 'hidden';
                    csrfInput.name = 'csrfmiddlewaretoken';
                    csrfInput.value = getCookie('csrftoken');
                    editForm.appendChild(csrfInput);

                    // Add comment body
                    const bodyInput = document.createElement('input');
                    bodyInput.type = 'hidden';
                    bodyInput.name = 'body';
                    bodyInput.value = document.getElementById('editCommentText').value;
                    editForm.appendChild(bodyInput);

                    // Update UI
                    const commentCard = document.getElementById(`comment${commentId}`).closest('.comment-card');
                    commentCard.classList.add('comment-pending');
                    
                    // Add pending notice
                    if (!commentCard.querySelector('.pending-notice')) {
                        const pendingNotice = document.createElement('div');
                        pendingNotice.className = 'pending-notice';
                        pendingNotice.innerHTML = `
                            <i class="fas fa-clock"></i>
                            Your edited comment is awaiting approval
                        `;
                        commentCard.appendChild(pendingNotice);
                    }

                    // Update comment text
                    document.getElementById(`comment${commentId}`).innerText = document.getElementById('editCommentText').value;

                    // Show notification and submit
                    showNotification('Comment updated successfully and awaiting approval', 'info');
                    editModal.hide();
                    document.body.appendChild(editForm);
                    editForm.submit();
                }, { once: true });
            });
        });

        // Delete button handlers
        Array.from(deleteButtons).forEach(button => {
            button.addEventListener("click", function(e) {
                const commentId = this.getAttribute("comment_id");
                const deleteForm = document.createElement('form');
                deleteForm.method = 'POST';
                deleteForm.action = `/post/${postSlug}/comment_delete/${commentId}/`;
                
                // Add CSRF token
                const csrfInput = document.createElement('input');
                csrfInput.type = 'hidden';
                csrfInput.name = 'csrfmiddlewaretoken';
                csrfInput.value = getCookie('csrftoken');
                deleteForm.appendChild(csrfInput);
        
                document.body.appendChild(deleteForm);
                
                // Set up delete confirmation
                deleteConfirm.onclick = function(e) {
                    e.preventDefault();
                    deleteForm.submit();
                };
                
                deleteModal.show();
            });
        });
    }
});