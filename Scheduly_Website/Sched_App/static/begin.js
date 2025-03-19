var secs=1000;
const LS=document.querySelector(".LOADING_CONTAINER");
window.onload=()=>{
    setTimeout(function(){
        LS.style.opacity="0";
        setTimeout(function(){
            LS.style.display="none"
        },.5*secs);
    },5*secs);
}