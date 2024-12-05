document.addEventListener('DOMContentLoaded', () => {
    const postSlugElement = document.getElementById("postSlug");
    if (!postSlugElement) return;

        // Initialize modals with error handling
        try {
            const editModal = document.getElementById("editModal");
            const deleteModal = document.getElementById("deleteModal");
            
            if (editModal) {
                const editModalInstance = new bootstrap.Modal(editModal);
            }
            if (deleteModal) {
                const deleteModalInstance = new bootstrap.Modal(deleteModal);
            }
        } catch (error) {
            console.warn('Modal initialization error:', error);
        }

    const postSlug = postSlugElement.getAttribute("data-slug");
    const editModal = document.getElementById("editModal");
    const deleteModal = document.getElementById("deleteModal");
    const editForm = document.getElementById("editForm");
    const deleteForm = document.getElementById("deleteForm");
    const commentsList = document.querySelector(".comments-list");

    // Initialize Bootstrap modals
    const editModalInstance = new bootstrap.Modal(editModal);
    const deleteModalInstance = new bootstrap.Modal(deleteModal);

    // Handle Edit functionality
    commentsList.addEventListener("click", (event) => {
        if (event.target.matches(".btn-edit")) {
            const commentId = event.target.getAttribute("data-comment-id");
            const commentContent = document.querySelector(`#comment${commentId} .comment-content`).innerText;
            document.getElementById("editCommentId").value = commentId;
            document.getElementById("editCommentText").value = commentContent.trim();
            editModalInstance.show();
        }
    });

    editForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const formData = new FormData(editForm);
        const response = await fetch(editForm.action, {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const commentId = document.getElementById("editCommentId").value;
            const commentCard = document.querySelector(`#comment${commentId}`).closest(".comment-card");
            commentCard.classList.add("comment-pending");
            const pendingNotice = commentCard.querySelector(".pending-notice");
            if (!pendingNotice) {
                commentCard.insertAdjacentHTML(
                    "beforeend",
                    `<div class="pending-notice">
                        <i class="fas fa-clock"></i>
                        Your edited comment is awaiting approval
                    </div>`
                );
            }
            document.querySelector(`#comment${commentId} .comment-content`).innerText = document.getElementById("editCommentText").value;
            showNotification("Comment updated successfully and awaiting approval", "info");
            editModalInstance.hide();
        } else {
            showNotification("Error updating comment. Please try again.", "error");
        }
    });

    // Handle Delete functionality
    commentsList.addEventListener("click", (event) => {
        if (event.target.matches(".btn-delete")) {
            const commentId = event.target.getAttribute("data-comment-id");
            document.getElementById("deleteCommentId").value = commentId;
            deleteModalInstance.show();
        }
    });

    deleteForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const formData = new FormData(deleteForm);
        const response = await fetch(deleteForm.action, {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const commentId = document.getElementById("deleteCommentId").value;
            document.querySelector(`#comment${commentId}`).closest(".comment-card").remove();
            showNotification("Comment deleted successfully", "success");
            deleteModalInstance.hide();
        } else {
            showNotification("Error deleting comment. Please try again.", "error");
        }
    });

    // Notification function
    function showNotification(message, type) {
        const notificationContainer = document.createElement("div");
        notificationContainer.classList.add("toast", "align-items-center", "text-white", "border-0", `bg-${type}`);
        notificationContainer.setAttribute("role", "alert");
        notificationContainer.setAttribute("aria-live", "assertive");
        notificationContainer.setAttribute("aria-atomic", "true");
        notificationContainer.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    <i class="fas ${type === "success" ? "fa-check-circle" : type === "error" ? "fa-exclamation-circle" : "fa-info-circle"} me-2"></i>
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        `;
        document.querySelector(".toast-container").appendChild(notificationContainer);
        const toast = new bootstrap.Toast(notificationContainer, { autohide: true, delay: 3000 });
        toast.show();
    }
});