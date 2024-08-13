document.addEventListener('DOMContentLoaded', () => {
  const editButtons = document.getElementsByClassName("btn-edit");
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteConfirm = document.getElementById("deleteConfirm");

  // Handle Edit button click
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let commentContent = document.getElementById(`comment${commentId}`).innerText;
      commentText.value = commentContent;
      submitButton.innerText = "Update";
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }

  // Handle Delete button click and show modal for confirmation
  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }
});


document.addEventListener('DOMContentLoaded', function () {
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteConfirm = document.getElementById("deleteConfirm");
  const postSlug = document.getElementById("postSlug").getAttribute("data-slug");

  for (let button of deleteButtons) {
    button.addEventListener("click", function (e) {
      let commentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `/${postSlug}/delete_comment/${commentId}/`;
      deleteModal.show();
    });
  }
});