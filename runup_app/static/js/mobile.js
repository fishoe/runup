"use strict";

// const adSection = document.querySelector('.ad-section');
// if (window.location.href !== "http://127.0.0.1:8000/"){
//   adSection.classList.add()
// }
// console.log(window.location.href);

// dropdown click function
function dropdownClickFunction(button, dropdown) {
  if (button.active) {
    dropdown.classList.remove("active");
  } else {
    dropdown.classList.add("active");
  }
  button.active = !button.active;
}

// category-menu
const categoryMenu = document.querySelector(".category-menu");
const all = document.querySelectorAll(".category-menu-dt");
const ddSection = document.querySelectorAll(".category-menu-dd-section");
// console.log(categoryMenu);

categoryMenu.addEventListener("click", (event) => {
  // console.log(event.target.firstChild.nextSibling.textContent);
  switch (event.target.firstChild.nextSibling.textContent) {
    case "후디&맨투맨":
      dropdownClickFunction(event.target, event.target.nextSibling.nextSibling);
      break;
    case "탑&티셔츠":
      dropdownClickFunction(event.target, event.target.nextSibling.nextSibling);
      break;
    case "팬츠&숏팬츠":
      dropdownClickFunction(event.target, event.target.nextSibling.nextSibling);
      break;
    case "레깅스":
      dropdownClickFunction(event.target, event.target.nextSibling.nextSibling);
      break;
    case "Accessory":
      dropdownClickFunction(event.target, event.target.nextSibling.nextSibling);
      break;
    case "스포츠 브라":
      dropdownClickFunction(event.target, event.target.nextSibling.nextSibling);
      break;
    case "가디건":
      dropdownClickFunction(event.target, event.target.nextSibling.nextSibling);
      break;
    case "Outer":
      dropdownClickFunction(event.target, event.target.nextSibling.nextSibling);
      break;
    case "스커트":
      dropdownClickFunction(event.target, event.target.nextSibling.nextSibling);
      break;
  }
});

// Category-menu Dropdown 실행
const categoryButton = document.querySelector(".footer-category");
const categoryBox = document.querySelector(".category-box");

categoryButton.addEventListener("click", () => {
  dropdownClickFunction(categoryButton, categoryBox);
});

categoryButton.active = false;

// MyPage dropdown-menu 실행
const myPageButton = document.querySelector(".footer-myPage");
const myPageBox = document.querySelector(".myPage-box");

myPageButton.addEventListener("click", () => {
  dropdownClickFunction(myPageButton, myPageBox);
});

myPageButton.active = false;

// likes dropdown-menu 실행
const likesButton = document.querySelector(".footer-likes");
const likesBox = document.querySelector(".likes-box");
likesButton.addEventListener("click", () => {
  dropdownClickFunction(likesButton, likesBox);
});

likesButton.active = false;

const footerItems = document.querySelector(".footer-items");
const myPages = document.querySelectorAll(".myPage");
const categories = document.querySelectorAll(".category");
const likes = document.querySelectorAll(".likes");

// console.log(categories);
// console.log(likes);
// console.log(myPages);

function footerItemsHandler() {
  console.log(footerItems);
  footerItems.addEventListener("click", (event) => {
    console.log(event.target);
  });
}
function init() {
  footerItemsHandler();
}
// init();

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

// category cancel button click event
const categoryCancelButton = document.querySelector(".category-cancel-icon");
categoryCancelButton.addEventListener("click", () => {
  window.history.back();
});
