function showAlert(element) {
    // Quita la clase active
    let links = document.querySelectorAll(".nav-links > li > a");
    for(let i = 0; i < links.length; i++){
        links[i].classList.remove("active");
    }

    // Presenta el texto.
    alert("Loading weather report... " + element.innerText);

    // Agrega la clase active.
    element.classList.add("active");
}

function acceptCookies(element) {
    // Obtiene el contenedor.
    let contenedorCookie = element.parentElement;

    // Remueve el elemento.
    contenedorCookie.remove();
}

function changeGrades(element){
    // Obtiene el elemento seleccionado.
    let valorSeleccionado = element.value;

    // Obtiene todos los span que se deben actualizar
    let maxSpan = document.querySelectorAll(".result-max > span");
    let minSpan = document.querySelectorAll(".result-min > span");

    // Cambia los valores.
    let valor = 0;
    for(let i = 0; i < maxSpan.length; i++){
        // Obtiene el valor que se debe cambiar.
        valor = parseFloat(maxSpan[i].innerText);
        
        // Cambia el valor
        maxSpan[i].innerText = changeValue(valorSeleccionado, valor);
    }
    for(let i = 0; i < minSpan.length; i++){
        // Obtiene el valor que se debe cambiar.
        valor = parseFloat(minSpan[i].innerText);
        
        // Cambia el valor
        minSpan[i].innerText = changeValue(valorSeleccionado, valor);
    }
}

function changeValue(option, valor){
    let resultado = 0;

    if (option === "gc") {
        // Cambia de grados fahrenheit a centígrados
        resultado = (valor - 32) * (5/9);
    } else {
        // Cambia de grados centígrados a fahrenheit
        resultado = (valor * 9/5) + 32;
    }
    
    //return Math.floor(resultado);
    //return resultado;
    return Math.round((resultado + Number.EPSILON) * 100) / 100;
}
