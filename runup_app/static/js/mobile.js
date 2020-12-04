'use strict';

// const adSection = document.querySelector('.ad-section');
// if (window.location.href !== "http://127.0.0.1:8000/"){
//   adSection.classList.add()
// }
// console.log(window.location.href);

// dropdown click function
function dropdownClickFunction(button, dropdown) {
  if (button.active) {
    dropdown.classList.remove('active');
  } else {
    dropdown.classList.add('active');
  }
  button.active = !button.active;
  // dropdownMenuSide.style.height = `${dropdownMenu.clientHeight}px`;
}

// Category-menu Dropdown 실행
const categoryMenu = document.querySelector('.category-menu');
const categoryButton = document.querySelector('.footer-category');
const categoryBox = document.querySelector('.category-box');

categoryButton.addEventListener('click', () => {
  dropdownClickFunction(categoryButton, categoryBox);
});

categoryButton.active = false;

// Men dropdown-menu
const menButton = document.querySelector('.men-button');
const categoryMenuMen = document.querySelector('.category-menu-men');

menButton.addEventListener('click', () => {
  dropdownClickFunction(menButton, categoryMenuMen);
});

menButton.active = false;

// Women dropdown-menu
const womenButton = document.querySelector('.women-button');
const categoryMenuWomen = document.querySelector('.category-menu-women');

womenButton.addEventListener('click', () => {
  dropdownClickFunction(womenButton, categoryMenuWomen);
});

womenButton.active = false;

// accessroy dropdown-menu
const accessoryButton = document.querySelector('.accessory-button');
const categoryMenuAccessory = document.querySelector('.category-menu-accessory');

accessoryButton.addEventListener('click', () => {
  dropdownClickFunction(accessoryButton, categoryMenuAccessory);
});

accessoryButton.active = false;

// MyPage dropdown-menu 실행
const myPageButton = document.querySelector('.footer-myPage');
const myPageBox = document.querySelector('.myPage-box');

myPageButton.addEventListener('click', () => {
  dropdownClickFunction(myPageButton, myPageBox);
});

myPageButton.active = false;

// categorySort dropdown-menu
const categorySortButton = document.querySelector('.category-sub-sort');
const categorySortDropdownMenu = document.querySelector('.categorySort-dropdown-menu');

categorySortButton.addEventListener('click', () => {
  dropdownClickFunction(categorySortButton, categorySortDropdownMenu);
});
categorySortButton.active = false;

// categoryFilter dropdown-menu
const categoryFilterButton = document.querySelector('.category-sub-filter');
const categoryFilterDropdownMenu = document.querySelector('.categoryFilter-dropdown-menu');

categoryFilterButton.addEventListener('click', () => {
  dropdownClickFunction(categoryFilterButton, categoryFilterDropdownMenu);
});
categoryFilterButton.active = false;

// category cancel button click event
const categoryCancelButton = document.querySelector('.category-cancel-icon');
categoryCancelButton.addEventListener('click', () => {
  window.history.back();
});
