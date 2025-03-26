import "./home.css" //t

const loadr=document.querySelector<HTMLDivElement>(".LOAD_CONT");
window.onload=()=>{
    setTimeout(function(){
        loadr.style.opacity="0";
        setTimeout(function(){
            loadr.style.display="none";
        },500);
    },5000);
}

document.addEventListener('DOMContentLoaded',()=>{
    let cX,cY,tgX,tgY=0;
    const bub=document.querySelector<HTMLDivElement>(".GRAD.I");
    function move(){
        cX+=(tgX-cX)/20;
        cY+=(tgY-cY)/20;
        bub.style.transform=`translate(${Math.round(cX)}px, ${Math.round(cY)}px)`;
        requestAnimationFrame(()=>{move();});
    }
    
    window.addEventListener('mousemove',(event)=>{
        tgX=event.clientX;
        tgY=event.clientY;});
    move();
});

