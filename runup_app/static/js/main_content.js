"use strict";

// 토글 구현 function
function toggle() {
  if (this.active) {
    this.classList.remove("active");
  } else {
    this.classList.add("active");
  }
  this.active = !this.active;
}

// 하트 버튼 클릭 이벤트
const heartButton = document.querySelectorAll(".heart-button");
function heartClickFunc() {
  heartButton.forEach((button) => {
    button.addEventListener("click", toggle);
    button.active;
  });
}

const csrf_token = document.querySelector("[name=csrfmiddlewaretoken]").value;
const productImageBoxLogin = document.querySelectorAll(".product-image-box-login");
const productImageBoxLogout = document.querySelectorAll(".product-image-box-logout");
let prod_id;
// 찜하기 버튼을 누르면 회원인지 아닌지 판단하는 함수, ajax처리
// 로그인을 했을경우 view의 like로 가서 like DB에 데이터를 추가해준다
productImageBoxLogin &&
  productImageBoxLogin.forEach((productImage) => {
    productImage.addEventListener("click", () => {
      prod_id = productImage.classList[1];
      fetch(`/${prod_id}/like`, {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-CSRFToken": csrf_token },
        body: JSON.stringify(),
      })
        .then((response) => response.json())
        // .then((data) => console.log("안녕"))
        .catch((error) => {
          console.log(error);
        });
    });
  });

productImageBoxLogout &&
  productImageBoxLogout.forEach((productImage) => {
    productImage.addEventListener("click", () => {
      prod_id = productImage.classList[1];
      // 로그인이 안됐을 경우 쿠키로 저장주는 함수로 보낸다.
      addCookie(prod_id);
    });
  });

// 저장된 쿠키값을 가져오는 함수
function getCookie(name) {
  let cname, cval;
  const clist = document.cookie.split(";");
  // console.log(clist);
  for (let i = 0; i < clist.length; i++) {
    cname = clist[i].substr(0, clist[i].indexOf("="));
    cval = clist[i].substr(clist[i].indexOf("=") + 1);
    cname = cname.replace(/^\s+|\s+$/g, ""); // 앞과 뒤의 공백 제거하기
    if (cname == name) {
      return cval; // unescape로 디코딩 후 값 리턴
    }
  }
  return null;
}

function addCookie(id) {
  const items = getCookie("like"); // 이미 저장된 값을 쿠키에서 가져오기
  const maxItemNum = 20; // 최대 저장 가능한 아이템개수
  // let expire = 1; // 쿠키값을 저장할 기간
  if (items != null) {
    const item_list = items.split(",");
    if (item_list[0] == "") {
      const letlikes = "like=" + id;
      document.cookie = letlikes;
      return letlikes;
    }
    for (let i = 0; i < item_list.length; i++) {
      if (item_list[i] == "" + id) {
        item_list.splice(i, 1);
        if (item_list.length == 0) {
          const letlikes = "like=";
          document.cookie = letlikes;
          return letlikes;
        }
        const letlikes = "like=" + item_list.join();
        document.cookie = letlikes;
        return letlikes;
      }
    }
    // like페이지 로드 시 item_array이용하여 product_id 불러오기
    item_list.push("" + id);
    const letlikes = "like=" + item_list.join();
    document.cookie = letlikes;
    return letlikes;
  } else {
    const letlikes = "like=" + id;
    document.cookie = letlikes;
    return letlikes;
  }
}

// init 함수
function init() {
  heartClickFunc();
}

init();
