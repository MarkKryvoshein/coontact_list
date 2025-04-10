document.addEventListener("DOMContentLoaded", function() {
  let selectedRow = null;
  let selectedContactId = null;

  const rows = document.querySelectorAll(".contact-row");
  const editButton = document.getElementById("editButton");

  rows.forEach(row => {
    row.addEventListener("click", function() {
      if (selectedRow) {
        selectedRow.classList.remove("table-active");
      }
      selectedRow = this;
      selectedRow.classList.add("table-active");

      selectedContactId = this.dataset.contactId;

      editButton.href = `/edit/${selectedContactId}`

    });
  });

});