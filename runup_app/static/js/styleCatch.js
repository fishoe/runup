"use strict";

const imageFile = document.querySelector("#photo");

document.addEventListener("DOMContentLoaded", () => {
  imageFile.addEventListener("change", (event) => {
    const files = event.target.files;
    const file = files[0];
    if (file) {
      const reader = new FileReader();
      const previewImage = document.querySelector("#pic");
      reader.onload = (event) => {
        previewImage.src = event.target.result;
      };
      reader.readAsDataURL(file);
      resizeImageFunc();
      // upLoadFunc();
    }
  });
});

// function upLoadFunc() {
// const resizePhoto = document.querySelector("#resizePhoto");
// console.log(resizePhoto.src);
// }

// image resizing function
function resizeImageFunc() {
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    const filesToUploads = imageFile.files;
    const file = filesToUploads[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        const image = document.createElement("img");
        image.src = event.target.result;

        const canvas = document.createElement("canvas");
        let context = canvas.getContext("2d");
        context.drawImage(image, 0, 0);

        const MAX_WIDTH = 190;
        const MAX_HEIGHT = 190;
        let width = image.width;
        let height = image.height;

        if (width > height) {
          if (width > MAX_WIDTH) {
            height *= MAX_WIDTH / width;
            width = MAX_WIDTH;
          }
        } else {
          if (height > MAX_HEIGHT) {
            width *= MAX_HEIGHT / height;
            height = MAX_HEIGHT;
          }
        }
        canvas.width = width;
        canvas.height = height;

        context = canvas.getContext("2d");
        context.drawImage(image, 0, 0, width, height);

        const dataurl = canvas.toDataURL(file.type);
        
        document.querySelector("#resizePhoto").src = dataurl;
        document.querySelector("#photo").value = URL.createObjectURL(dataurl);
      };
      reader.readAsDataURL(file);
      // console.log(file);
    }
  } else {
    alert("이 파일 형식은 저희 홈페이지에서 지원하지 않는 파일 형식입니다.");
  }
}

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
