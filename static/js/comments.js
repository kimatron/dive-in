document.addEventListener('DOMContentLoaded', () => {
  const editButtons = document.getElementsByClassName("btn-edit");
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteConfirm = document.getElementById("deleteConfirm");

  // Ensure postSlug is available
  const postSlugElement = document.getElementById("postSlug");
  if (postSlugElement) {
    const postSlug = postSlugElement.getAttribute("data-slug");

    // Handle Edit button click
    for (let button of editButtons) {
      button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("comment_id");
        const commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `/post/${postSlug}/comment_edit/${commentId}/`); // Ensure this matches your URL pattern
      });
    }

    // Handle Delete button click and show modal for confirmation
    for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `/post/${postSlug}/comment_delete/${commentId}/`; // Ensure this matches your URL pattern
        deleteModal.show();
      });
    }
  } else {
    console.error("Element with ID 'postSlug' not found.");
  }
});