"use strict";

// *--------------------- SLIDING FUNCTIONALITY USING INTERSECTION OBSERVER API ---------------------* //
const homeSections = document.querySelectorAll(".container--home--section");

const options = {
  rootMargin: "0px",
  threshold: 0.15,
};

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting && entry.intersectionRatio > 0.15) {
      const sectionImg = entry.target.querySelector(".container__image--wrapper");
      const sectionTxt = entry.target.querySelector(".container__text--wrapper");
      sectionImg.style.transform = "translateX(0)";
      sectionImg.style.opacity = 1;
      sectionTxt.style.transform = "translateX(0)";
      sectionTxt.style.opacity = 1;
    }
  });
}, options);

homeSections.forEach(section => {
  observer.observe(section);
});

// *-------------------------- FUNCTIONALITY TO CREATE NEW NOTES ---------------------------* //
const noteForm = document.querySelector(".new--note--form--container form");
const titleField = document.querySelector("form #title");
const contentField = document.querySelector("form textarea");
const noteCards = document.querySelector(".notes__cards");

// Function to send note data
const createNote = note => {
  const promise = new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();

    xhr.responseType = "json";
    xhr.timeout = 3000;
    xhr.open("post", "/home", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(note));

    xhr.onload = () => {
      xhr.status === 200 ? resolve(xhr.response) : reject(xhr.response);
    };

    xhr.ontimeout = timeError => reject(timeError);
    xhr.onerror = err => reject(err);
  });

  return promise;
};

// Function to add note in UI
const addNote = function (note) {
  createNote(note)
    .then(data => {
      const noteHtml = `<div class="note__card" id="note__card--${data.id}"><div><span class="note__date">${data.note_date}
          </span><button class="note__delete--btn"><ion-icon name="trash"></ion-icon></button></div><div>
         <h3 class="note__card--title">${data.title}</h3><p class="note__card--content">${data.content}</p></div></div>`;
      noteCards.insertAdjacentHTML("afterbegin", noteHtml);
    })
    .catch(err => console.error(err));
};

// Event Handler for Note Form Submission
noteForm.addEventListener("submit", function (e) {
  e.preventDefault();

  const [title, content] = [titleField.value.trim(), contentField.value.trim()];
  if (title.length > 0) {
    titleField.value = "";
    contentField.value = "";
    addNote({ title, content });
  }
});

// *------------------- Functionality to Delete notes --------------------*
