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
// const infinite = new Waypoint.Infinite({
//   element: document.querySelector(".infinite-container"),
  // element: $(".infinite-container")[0],
// });



// 상품 넘어갈때 나오는 에니메이션 효과 코드 주석 onclick event를 사용해서 했었음.
// function animation(targetUrl) {
//   var maskHeight = $(document).height();
//   var windowHeight = $(window).height();
//   var maskWidth = $(document).width();
//   var height = $(document).scrollTop();

//   var mask = "<div id='mask' style='position:absolute; z-index:9000; background-color:#000000; display:none; left:0; top:0;'></div>";
//   var loadingImg = "";
//   var delayTimeMillis = 1200;

//   loadingImg += "<div id='loadingImg' style='position:absolute; left:10%; display:none; z-index:10000;'>";
//   loadingImg += " <img src='https://mir-s3-cdn-cf.behance.net/project_modules/disp/35771931234507.564a1d2403b3a.gif'/>";
//   loadingImg += "</div>";

//   $("form").append(mask).append(loadingImg);

//   $("#mask").css({
//     width: maskWidth,
//     height: maskHeight,
//     opacity: "0.4",
//   });

//   $("#mask").show();

//   if (height == 0) {
//     $("#loadingImg").css({
//       top: windowHeight / 3,
//     });
//   } else {
//     $("#loadingImg").css({
//       top: height + windowHeight / 3,
//     });
//   }

//   $("#loadingImg").show();

//   // 실행 지연
//   setTimeout(function () {
//     location.href = targetUrl;
//   }, delayTimeMillis);
// }
