var myIndex = 0;
carousel();
//성의 없는 변수 이름 수정 요망
function carousel() {
  var i;
  var x = document.getElementsByClassName("banner-img");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  //루프 개선 아이템이 없는 상태에 대한 개선 필요.
  if (x.length == 0) return;
  myIndex++;
  if (myIndex > x.length) {myIndex = 1;}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 2000); // Change image every 2 seconds
}
