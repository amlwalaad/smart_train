let problem = document.querySelector(".last");
let otl = document.querySelector(".first");
let middleBtn = document.querySelector(".middle");
let twoBtn = document.querySelector(".two-btn");
let back = document.querySelector(".back");
let sideMessage = document.querySelector(".translation");
let mess = document.querySelector(".two-Msg");
let table = document.querySelector(".my-table");

problem.addEventListener("click",function(){
  twoBtn.style.display = "flex";
  otl.style.display = "none";
  middleBtn.style.display = "none";
  sideMessage.style.display = "none";
  table.style.display = "none";
});
back.addEventListener("click",function(){
  otl.style.display = "block";
  middleBtn.style.display = "block";
  problem.style.display = "block";
  twoBtn.style.display =  "none";
  sideMessage.style.display = "none";
  mess.style.display = "none";
  table.style.display = "flex";
});

otl.addEventListener("click",function(){
  sideMessage.style.display = "flex";
  otl.style.display = "none";
  middleBtn.style.display = "none";
  problem.style.display = "none";

});

middleBtn.addEventListener("click",function(){
  problem.style.display = "none";
  otl.style.display = "none";
  mess.style.display = "flex";
  sideMessage.style.display = "none";
  table.style.display = "none";
});
