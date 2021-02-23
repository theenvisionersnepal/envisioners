function showMore(){
    document.getElementById("showmore").style.clipPath = "polygon(0 0, 100% 0, 100% 100%, 0% 100%)";
}
function showLess(){
    document.getElementById("showmore").style.clipPath = "polygon(100% 0, 100% 0, 100% 100%, 100% 100%)";
}
function showOverlay(){
    document.getElementById("menu-overlay").style.clipPath = "polygon(100% 100%, 100% 0, 0 0, 0 100%)";
}
function closeOverlay(){
    document.getElementById("menu-overlay").style.clipPath = "polygon(0 0, 100% 0, 0 0, 0 100%)";
}