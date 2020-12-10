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

// category-menu
const categoryMenu = document.querySelector(".category-menu");
// const all = document.querySelectorAll(".category-menu-dt");

function categorySubDropDown() {
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
          grayColorChange(categoryButton);
          scrollControl();
        } else {
          checkButton = document.querySelector(`.footer-${checkTarget}`);
          checkBox = document.querySelector(`.${checkTarget}-box`);
          onClickRemove(checkButton, checkBox);
          whiteColorChange(checkButton);
          onClickAdd(categoryButton, categoryBox);
          grayColorChange(categoryButton);
          scrollControl();
        }
        checkTarget = event.target.classList[0];
        // console.log(checkTarget);
        break;
      case "likes":
        // checkTarget을 확인 만약 비어있다면, onClickAdd()
        if (!checkTarget) {
          onClickAdd(likesButton, likesBox);
          grayColorChange(likesButton);
          scrollControl();
        } else {
          checkButton = document.querySelector(`.footer-${checkTarget}`);
          checkBox = document.querySelector(`.${checkTarget}-box`);
          onClickRemove(checkButton, checkBox);
          whiteColorChange(checkButton);
          onClickAdd(likesButton, likesBox);
          grayColorChange(likesButton);
          scrollControl();
        }
        checkTarget = event.target.classList[0];
        break;
      case "myPage":
        // checkTarget을 확인 만약 비어있다면, onClickAdd()
        if (!checkTarget) {
          onClickAdd(myPageButton, myPageBox);
          grayColorChange(myPageButton);
          scrollControl();
        } else {
          checkButton = document.querySelector(`.footer-${checkTarget}`);
          checkBox = document.querySelector(`.${checkTarget}-box`);
          onClickRemove(checkButton, checkBox);
          whiteColorChange(checkButton);
          onClickAdd(myPageButton, myPageBox);
          grayColorChange(myPageButton);
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
