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

  // Initialize Toasts if they exist
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

      // Add click event listeners to edit buttons
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

            // Update UI before submitting
            const commentCard = document.getElementById(`comment${commentId}`).closest('.comment-card');
            commentCard.classList.add('comment-pending');
            
            // Add pending notice if it doesn't exist
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

            // Show notification
            showNotification('Comment updated successfully and awaiting approval', 'info');
            
            // Hide modal
            editModal.hide();

            // Submit form
            document.body.appendChild(editForm);
            editForm.submit();
        }, { once: true });
    });
});

      // Add click event listeners to delete buttons
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
    
            // Add to document
            document.body.appendChild(deleteForm);
            
            // Set up delete confirmation
            deleteConfirm.onclick = function(e) {
                e.preventDefault();
                deleteForm.submit();
            };
            
            // Show modal
            deleteModal.show();
        });
    });
  }
});

// Helper function to handle notifications
function showNotification(message, type = 'success') {
  const toastContainer = document.createElement('div');
  toastContainer.className = 'toast-container position-fixed bottom-0 end-0 p-3';
  toastContainer.style.zIndex = '1050';

  const toast = document.createElement('div');
  toast.className = `toast align-items-center text-white bg-${type} border-0`;
  toast.setAttribute('role', 'alert');
  toast.setAttribute('aria-live', 'assertive');
  toast.setAttribute('aria-atomic', 'true');

  const content = `
      <div class="d-flex">
          <div class="toast-body">
              <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'} me-2"></i>
              ${message}
          </div>
          <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
  `;

  toast.innerHTML = content;
  toastContainer.appendChild(toast);
  document.body.appendChild(toastContainer);

  const bsToast = new bootstrap.Toast(toast, {
      autohide: true,
      delay: 3000
  });

  bsToast.show();

  toast.addEventListener('hidden.bs.toast', () => {
      toastContainer.remove();
  });
}

// Helper function to get CSRF token
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