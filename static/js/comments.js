document.addEventListener('DOMContentLoaded', () => {
  // Initialize Elements
  const editButtons = document.getElementsByClassName("btn-edit");
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteConfirm = document.getElementById("deleteConfirm");

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
              // Get the comment ID from the button's attribute
              const commentId = this.getAttribute("comment_id");
              // Get the comment content
              const commentContent = document.getElementById(`comment${commentId}`).innerText;
              // Update the form
              commentText.value = commentContent;
              submitButton.innerText = "Update";
              commentForm.setAttribute("action", `/post/${postSlug}/comment_edit/${commentId}/`);
          });
      });

      // Add click event listeners to delete buttons
      Array.from(deleteButtons).forEach(button => {
          button.addEventListener("click", function(e) {
              // Get the comment ID from the button's attribute
              const commentId = this.getAttribute("comment_id");
              // Set the delete confirmation link
              deleteConfirm.href = `/post/${postSlug}/comment_delete/${commentId}/`;
              // Show the modal
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