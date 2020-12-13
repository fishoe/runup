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
const categorySortDropdownMenu = document.querySelector(".categorySort-dropdown-menu");

categorySortButton.addEventListener("click", () => {
  dropdownClickFunction(categorySortButton, categorySortDropdownMenu);
});
categorySortButton.active = false;

// categoryFilter dropdown-menu
const categoryFilterButton = document.querySelector(".category-sub-filter");
const categoryFilterDropdownMenu = document.querySelector(".categoryFilter-dropdown-menu");

categoryFilterButton.addEventListener("click", () => {
  dropdownClickFunction(categoryFilterButton, categoryFilterDropdownMenu);
});
categoryFilterButton.active = false;

// heart icon fill & border
const heartButton = document.querySelectorAll(".heart-button");

heartButton.forEach((button) => {
  button.addEventListener("click", toggle);
  button.active;
});

function toggle() {
  if (this.active) {
    this.classList.remove("active");
  } else {
    this.classList.add("active");
  }
  this.active = !this.active;
}

// 무한 스크롤 구현?
if (window.console != null) {
  console.log("console is exist");
} else {
  coneolse.log("console is null");
}
var infinite = new Waypoint.Infinite({
  element: $(".infinite-container")[0],
});
