const IMAGE_WIDTH = 1400;
let imgIndex;
let pos = 0;

function init() {
  document.querySelector(".slide_button_1").setAttribute("disabled", "true");
}

function click_Btn1() {
  enable_all();
  document.querySelector(".slide_button_1").setAttribute("disabled", "true");
  pos = 0;
  document.querySelector(
    ".slide_image_container"
  ).style.transform = `translateX(${pos}px)`;
}

function click_Btn2() {
  enable_all();
  document.querySelector(".slide_button_2").setAttribute("disabled", "true");
  pos = -1 * IMAGE_WIDTH;
  document.querySelector(
    ".slide_image_container"
  ).style.transform = `translateX(${pos}px)`;
}

function click_Btn3() {
  enable_all();
  document.querySelector(".slide_button_3").setAttribute("disabled", "true");
  pos = -2 * IMAGE_WIDTH;
  document.querySelector(
    ".slide_image_container"
  ).style.transform = `translateX(${pos}px)`;
}

function click_Btn4() {
  enable_all();
  document.querySelector(".slide_button_4").setAttribute("disabled", "true");
  pos = -3 * IMAGE_WIDTH;
  document.querySelector(
    ".slide_image_container"
  ).style.transform = `translateX(${pos}px)`;
}

function enable_all() {
  document.querySelector(".slide_button_1").removeAttribute("disabled");
  document.querySelector(".slide_button_2").removeAttribute("disabled");
  document.querySelector(".slide_button_3").removeAttribute("disabled");
  document.querySelector(".slide_button_4").removeAttribute("disabled");
}

setTimeout(() => init(), 10);
