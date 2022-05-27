let inner = document.querySelector(".inner");
let outer = document.querySelector(".outer");
let theSwitch = document.querySelector(".switch");
let innerMsg = document.querySelector(".innerMsg");
let outerMsg = document.querySelector(".outerMsg");
let translation = document.querySelector(".translation");
let mapstyle = document.getElementById("map");

inner.addEventListener("click",function (){
    innerMsg.style.display="flex";
    mapstyle.style.display="none";
});
outer.addEventListener("click",function (){
    innerMsg.style.display="none";
    mapstyle.style.display="none";
    outerMsg.style.display="flex";
});
theSwitch.addEventListener("click",function (){
    innerMsg.style.display="none";
    outerMsg.style.display="none";
    translation.style.display="flex";
});