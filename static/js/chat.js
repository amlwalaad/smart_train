
let shakwa = document.querySelector(".check-complaints");
let otl = document.querySelector(".damage");
let middleBtn = document.querySelector(".connect-train");
let errors = document.querySelector(".errors");
let whiteBtn = document.querySelector(".white");
let closeBtn = document.querySelector(".close");
let secCloseBtn = document.querySelector(".close2");
let side = document.querySelector(".my-side");
let side2 = document.querySelector(".my-side2");

shakwa.addEventListener("click",function(){
  side.style.display = "block";
  otl.style.display= "none";
  middleBtn.style.display = "none";
});

closeBtn.addEventListener("click",function(){
  errors.style.display = "none";
  whiteBtn.style.display = "none";
  side.style.display = "none";
  side2.style.display = "none";
  shakwa.style.display = "block";
  middleBtn.style.display = "block";
  otl.style.display = "block";
});

middleBtn.addEventListener("click",function(){
  side2.style.display = "block";
  shakwa.style.display = "none";
  otl.style.display = "none";
});

otl.addEventListener("click",function(){
  errors.style.display = "grid";
  shakwa.style.display = "none";
  middleBtn.style.display = "none";
  whiteBtn.style.display = "block";
});
closeBtn.addEventListener("click",function(){
  side.style.display = "none";
  middleBtn.style.display = "block";
  otl.style.display = "block";
});
secCloseBtn.addEventListener("click",function(){
  side2.style.display = "none";
  shakwa.style.display = "block";
  otl.style.display = "block";
})