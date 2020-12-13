"use strict";

// men women switch toggle
const switchButton = document.querySelector(".men-women-switch");

function toggle() {
  if (this.active) {
    this.classList.remove("active");
  } else {
    this.classList.add("active");
  }
  this.active = !this.active;
}

switchButton.addEventListener("click", toggle);

// dropdown click function
function dropdownClickFunction(button, dropdown) {
  if (button.active) {
    dropdown.classList.remove("active");
  } else {
    dropdown.classList.add("active");
  }
  button.active = !button.active;
}

function categoryDropdownClickFunction(button, dropdown) {
  if (button.active) {
    dropdown.classList.remove("category-menu-dd-section-active");
  } else {
    dropdown.classList.add("category-menu-dd-section-active");
  }
  button.active = !button.active;
}

// category-menu
const categoryMenu = document.querySelector(".category-menu");
// 각 카테고리의 드랍다운 매뉴들 --> 추후에 매뉴가 바뀌면 확인 해봐야할 듯...?
const menuDropdown1 = document.querySelector(".menu-dropdown-1"); // 후디 맨투맨
const menuDropdown2 = document.querySelector(".menu-dropdown-2"); // 탑티셔츠
const menuDropdown3 = document.querySelector(".menu-dropdown-3"); // 팬츠 숏팬츠
const menuDropdown4 = document.querySelector(".menu-dropdown-4"); // 레깅스
const menuDropdown5 = document.querySelector(".menu-dropdown-5"); // 악세사리
const menuDropdown6 = document.querySelector(".menu-dropdown-6"); // 스포츠 브라
const menuDropdown7 = document.querySelector(".menu-dropdown-7"); // 가디건
const menuDropdown8 = document.querySelector(".menu-dropdown-8"); // 아우터
const menuDropdown9 = document.querySelector(".menu-dropdown-9"); // 스커트

function categorySubDropDown() {
  categoryMenu.addEventListener("click", (event) => {
    switch (event.target.classList[0]) {
      // 후디 맨투맨
      case "menu-id-1":
        categoryDropdownClickFunction(event.target, menuDropdown1);
        break;
      // 탑 티셔츠
      case "menu-id-2":
        categoryDropdownClickFunction(event.target, menuDropdown2);
        break;
      // 팬츠 숏팬츠
      case "menu-id-3":
        categoryDropdownClickFunction(event.target, menuDropdown3);
        break;
      // 레깅스
      case "menu-id-4":
        categoryDropdownClickFunction(event.target, menuDropdown4);
        break;
      // 악세사리
      case "menu-id-5":
        categoryDropdownClickFunction(event.target, menuDropdown5);
        break;
      // 스포츠 브라
      case "menu-id-6":
        categoryDropdownClickFunction(event.target, menuDropdown6);
        break;
      // 가디건
      case "menu-id-7":
        categoryDropdownClickFunction(event.target, menuDropdown7);
        break;
      // 아우터
      case "menu-id-8":
        categoryDropdownClickFunction(event.target, menuDropdown8);
        break;
      // 스커트
      case "menu-id-9":
        categoryDropdownClickFunction(event.target, menuDropdown9);
        break;
    }
  });
}

function onClickRemove(button, dropdown) {
  if (button.active) {
    dropdown.classList.remove("active");
  }
  button.active = !button.active;
}

function onClickAdd(button, dropdown) {
  if (!button.active) {
    dropdown.classList.add("active");
  }
  button.active = !button.active;
}

function grayColorChange(button) {
  button.style.backgroundColor = "#eff2f7";
}

function whiteColorChange(button) {
  button.style.backgroundColor = "#fff";
}

function scrollControl() {
  window.scroll({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
}

const footerItems = document.querySelector(".footer-items");
const categoryButton = document.querySelector(".footer-category");
const categoryBox = document.querySelector(".category-box");
const likesButton = document.querySelector(".footer-likes");
const likesBox = document.querySelector(".likes-box");
const myPageButton = document.querySelector(".footer-myPage");
const myPageBox = document.querySelector(".myPage-box");

// 빈 변수 선언
let checkTarget = "";
let checkButton;
let checkBox;

// footer banner click event 한쪽 눌렀을때 눌린 베너 끄고 새로운 베너 오픈 하는 이벤트 function
function footerItemsHandler() {
  footerItems.addEventListener("click", (event) => {
    switch (event.target.classList[0]) {
      case "category":
        // event.target이 'category'일 경우
        // checkTarget을 확인 만약 비어있다면, onClickAdd()
        if (!checkTarget) {
          onClickAdd(categoryButton, categoryBox);
          // grayColorChange(categoryButton);
          scrollControl();
        } else {
          checkButton = document.querySelector(`.footer-${checkTarget}`);
          checkBox = document.querySelector(`.${checkTarget}-box`);
          onClickRemove(checkButton, checkBox);
          whiteColorChange(checkButton);
          onClickAdd(categoryButton, categoryBox);
          // grayColorChange(categoryButton);
          scrollControl();
        }
        checkTarget = event.target.classList[0];
        // console.log(checkTarget);
        break;
      case "likes":
        // checkTarget을 확인 만약 비어있다면, onClickAdd()
        if (!checkTarget) {
          onClickAdd(likesButton, likesBox);
          // grayColorChange(likesButton);
          scrollControl();
        } else {
          checkButton = document.querySelector(`.footer-${checkTarget}`);
          checkBox = document.querySelector(`.${checkTarget}-box`);
          onClickRemove(checkButton, checkBox);
          whiteColorChange(checkButton);
          onClickAdd(likesButton, likesBox);
          // grayColorChange(likesButton);
          scrollControl();
        }
        checkTarget = event.target.classList[0];
        break;
      case "myPage":
        // checkTarget을 확인 만약 비어있다면, onClickAdd()
        if (!checkTarget) {
          onClickAdd(myPageButton, myPageBox);
          // grayColorChange(myPageButton);
          scrollControl();
        } else {
          checkButton = document.querySelector(`.footer-${checkTarget}`);
          checkBox = document.querySelector(`.${checkTarget}-box`);
          onClickRemove(checkButton, checkBox);
          whiteColorChange(checkButton);
          onClickAdd(myPageButton, myPageBox);
          // grayColorChange(myPageButton);
          scrollControl();
        }
        checkTarget = event.target.classList[0];
        break;
    }
  });
}

function init() {
  footerItemsHandler();
  categorySubDropDown();
}
init();
