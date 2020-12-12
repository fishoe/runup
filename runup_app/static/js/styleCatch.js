"use strict";

function styleCatchFunc() {
  $(document).ready(function () {
    if (!("url" in window) && "webkitURL" in window) {
      window.URL = window.webkitURL;
    }
    $("#photo").change(function (e) {
      $("#pic").attr("src", URL.createObjectURL(e.target.files[0]));
    });
  });
  $(document).ready(function () {
    if (!("url" in window) && "webkitURL" in window) {
      window.URL = window.webkitURL;
    }
    $("#album").change(function (e) {
      $("#pic").attr("src", URL.createObjectURL(e.target.files[0]));
    });
  });
  //$('.styleCatch-camera').on('click',function(){$('#photo').click();});
}

const styleCatchInput = document.querySelector("#photo");
const styleCatchImage = document.querySelector("#pic");
const styleCatchComplete = document.querySelector(".styleCatch-complete");

// styleCatch화면에서 사진 업로드시 발생하는 이벤트.
function completeColorChange() {
  styleCatchInput.addEventListener("change", () => {
    if (styleCatchImage.src) {
      styleCatchComplete.classList.remove("active");
    } else {
      styleCatchComplete.classList.add("active");
    }
  });
}

function init() {
  styleCatchFunc();
  completeColorChange();
}

init();
