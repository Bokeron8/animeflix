// Create video element
const video = document.getElementById('video');
const servers_btn = document.querySelectorAll("li button");

Array.from(servers_btn).forEach(btn => {
    
    btn.addEventListener("click", function(){
        video.src = btn.value;
    })
});


const box = document.getElementById('box');
