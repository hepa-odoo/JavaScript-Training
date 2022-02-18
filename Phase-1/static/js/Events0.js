document.addEventListener("mousemove",(event)=>{
    document.getElementById("text-result").innerHTML=('Cursor at: '+event.pageX+', '+event.pageY+'<br/>');
});

const myOwnEvent = new Event("myEvent");
document.addEventListener('myEvent', ()=>{
    document.getElementById("text-result2").innerHTML+=("my own event triggered!!<br/>");
});

setInterval(()=>document.dispatchEvent(myOwnEvent), 2500);