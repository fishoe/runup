'use strict';

// infinite-item click event 오래 클릭 했을때, 모달창 띄우기?
// 필요한 변수 선언
const imageBox = document.querySelectorAll(".img_box");
let isTouch = false;
let counter = 0;
let pressTimer;

// 각각의 아이템에게 이벤트 주기.
imageBox.forEach((item) => {
  item.addEventListener("touchstart", () => {
    console.log("touchstart");
    const aFirstChildHref = item.firstChild.nextSibling.classList[2];
    const aSecondChildHref = item.firstChild.nextSibling.classList[1];
    isTouch = true;
    pressTimer = setInterval(() => {
      counter++;
      itemClickFunc(item, aFirstChildHref, aSecondChildHref);
    }, 500);
  });

  item.addEventListener("touchend", () => {
    console.log("touchend");
    clearInterval(pressTimer);
    isTouch = false;
    counter = 0;
  });
});

// 이미지 롱클릭 조건 함수
function itemClickFunc(item, aFirstChildHref, aSecondChildHref) {
  if (isTouch && counter > 1) {
    console.log("눌렸습니다.");
    clearInterval(pressTimer);
    createElementFunc(item, aFirstChildHref, aSecondChildHref);
  }
  // 롱클릭 후 dropdown menu 제거 이벤트
  const dropdownDeleteButton = document.querySelector('.item-dropdown-delete-button');

  dropdownDeleteButton && dropdownDeleteButton.addEventListener('click', () => {
    const dropdownUl = document.querySelector('.item-dropdown-ul')
    dropdownUl.remove();
    dropdownDeleteButton.remove();
  });

}

// createElement function
function createElementFunc(item, aFirstChildHref, aSecondChildHref) {
  let parentUl = document.createElement("ul");
  parentUl.setAttribute("class", "item-dropdown-ul");

  let deleteButton = document.createElement('div');
  deleteButton.setAttribute('class', 'item-dropdown-delete-button');
  let height = document.querySelector('body').offsetHeight+'px'
  deleteButton.style.height = height;
  document.querySelector("body").append(deleteButton);

  let firstChildLi = document.createElement("li");
  firstChildLi.setAttribute("class", "item-dropdown-li");
  
  let firstChildAtag = document.createElement('a');
  firstChildAtag.textContent = "해당 상품 보러가기";
  firstChildAtag.setAttribute('href', aFirstChildHref);
  firstChildLi.append(firstChildAtag);

  parentUl.append(firstChildLi);

  let secondChildLi = document.createElement("li");
  secondChildLi.setAttribute("class", "item-dropdown-li");
  
  let secondChildAtag = document.createElement('a');
  secondChildAtag.textContent = "AI추천 결과 보러가기";
  secondChildAtag.setAttribute('href', aSecondChildHref);
  secondChildLi.append(secondChildAtag);

  parentUl.append(secondChildLi);

  item.append(parentUl);
}
