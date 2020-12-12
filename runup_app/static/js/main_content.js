"use strict";

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
