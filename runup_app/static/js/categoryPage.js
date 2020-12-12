"use strict";

// dropdown click function
function dropdownClickFunction(button, dropdown) {
  if (button.active) {
    dropdown.classList.remove("active");
  } else {
    dropdown.classList.add("active");
  }
  button.active = !button.active;
}

// categorySort dropdown-menu
const categorySortButton = document.querySelector(".category-sub-sort");
const categorySortDropdownMenu = document.querySelector(
  ".categorySort-dropdown-menu"
);

categorySortButton.addEventListener("click", () => {
  dropdownClickFunction(categorySortButton, categorySortDropdownMenu);
});
categorySortButton.active = false;

// categoryFilter dropdown-menu
const categoryFilterButton = document.querySelector(".category-sub-filter");
const categoryFilterDropdownMenu = document.querySelector(
  ".categoryFilter-dropdown-menu"
);

categoryFilterButton.addEventListener("click", () => {
  dropdownClickFunction(categoryFilterButton, categoryFilterDropdownMenu);
});
categoryFilterButton.active = false;

// category cancel button click event
// const categoryCancelButton = document.querySelector(".category-cancel-icon");
// categoryCancelButton.addEventListener("click", () => {
//   window.history.back();
// });
