function imprimirImpares() {
    let initial = parseInt(document.getElementById("txtInitial").value);
    let end = parseInt(document.getElementById("txtEnd").value);

    console.log("imprimirImpares");
    let result = "";
    for(let i = initial; i <= end; i++) {
        if(i % 2 !== 0) {
            console.log(i);
            result += "<p>" + i + "</p>";
        }
    }

    let rst = document.getElementById("rslImprimirImpares");
    rst.innerHTML = result;
    //rst.insertAdjacentHTML("beforeend", result);
}

function disminuirMultiplos() {
    let initial = parseInt(document.getElementById("txtInitialM").value);
    let end = parseInt(document.getElementById("txtEndM").value);
    let multiplos = parseInt(document.getElementById("txtMultiplos").value);

    console.log("disminuirMultiplos");
    let result = "";
    for(let i = initial; i >= end; i--) {
        if(i % multiplos === 0) {
            console.log(i);
            result += "<p>" + i + "</p>";
        }
    }

    let rst = document.getElementById("rslDisminuirMultiplos");
    rst.innerHTML = result;
    //rst.insertAdjacentHTML("beforeend", result);
}

function imprimirSecuencia() {
    console.log("imprimirSecuencia");

    let result = "";
    for(let i = 4; i > -4; i-=1.5) {
        console.log(i);
        result += "<p>" + i + "</p>";
    }

    let rst = document.getElementById("rslSecuencia");
    rst.innerHTML = result;
    //rst.insertAdjacentHTML("beforeend", result);
}

function sigma() {
    console.log("sigma");

    let end = parseInt(document.getElementById("txtUltimoS").value);

    let total = 0
    for(let i = 1; i <= end; i++) {
        total += i;
    }

    console.log(total);
    let rst = document.getElementById("rslSigma");
    rst.innerHTML = "<p>" + total + "</p>";
    //rst.insertAdjacentHTML("beforeend", "<p>" + total + "</p>");
}

function factorial() {
    console.log("factorial");

    let end = parseInt(document.getElementById("txtUltimoF").value);

    let total = 1
    for(let i = 1; i <= end; i++) {
        total *= i;
    }

    console.log(total);
    let rst = document.getElementById("rslFactorial");
    rst.innerHTML = "<p>" + total + "</p>";
    //rst.insertAdjacentHTML("beforeend", "<p>" + total + "</p>");
}