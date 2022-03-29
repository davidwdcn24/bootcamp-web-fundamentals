let changeImage = (element) => {
    if (element.src.indexOf("/cat") > -1)
        element.src = element.src.replace("/cat", "/ninja");
    else
        element.src = element.src.replace("/ninja", "/cat");
}

let elementsImg = document.querySelectorAll("img");
elementsImg.forEach(function (img){
    img.addEventListener('click', function(){
        changeImage(img);
    });
});

let chkDirection = document.getElementById("chkDirection");
let index = chkDirection.checked ? 0 : 4;
let intervalChange = null;

let start = () => {
    intervalChange = setInterval(function(){
        console.log(index);
        if (chkDirection.checked && index === 5)
            index = 0;
        else if (!chkDirection.checked && index === -1)
            index = 4;

        elementsImg[index].click();

        if (chkDirection.checked)
            index++;
        else 
            index--;
    }, 1000);
}

let stop = () => {
    if(intervalChange)
        clearInterval(intervalChange);
}

document.getElementById("btnStart").addEventListener('click', function(){
    start();
});

document.getElementById("btnStop").addEventListener('click', function(){
    stop();
});

chkDirection.addEventListener('change', function(){
    //stop();
    if (chkDirection.checked)
        index++;
    else 
        index--;
    //start();
});