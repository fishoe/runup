"use strict";

// function dropdownClickFunction()

// Get the modal
const search_modal = document.querySelector(".search-modal");

// Get the button that opens the modal
const search_btn = document.querySelector(".header-search");

// Get the <span> element that closes the modal
const search_cls = document.querySelector(".search-close");

// When the user clicks on the button, open the modal
search_btn.addEventListener("click",() => {
  search_modal.style.display = "block";
});
search_btn.active = false;

// When the user clicks on <span> (x), close the modal
search_cls.addEventListener("click",() => {
  search_modal.style.display = "none";
});
search_cls.active = false;

// // When the user clicks anywhere outside of the modal, close it
// window.addEventListener("click",() => {
//   if (event.target == search_modal) {
//     search_modal.style.display = "none";
//   }
// });