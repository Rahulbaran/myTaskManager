"use strict";

const noteForm = document.querySelector("new--note--form--container form");
const titleField = document.querySelector("form .title");
const contentField = document.querySelector("form textarea");

// Event Handler for Note Form Submission
noteForm.addEventListener("submit", function (e) {
  e.preventDefault();

  const [title, content] = [titleField.value.trim(), contentField.value.trim()];

  if (title.length > 0) {
  }
});
