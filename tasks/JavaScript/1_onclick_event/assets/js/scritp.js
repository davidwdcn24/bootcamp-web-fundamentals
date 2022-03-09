function changeTextLogin(){
    // Obtiene el botón de login.
    var btnLogin = document.getElementById("btnLogin");

    // Cambia el texto.
    if(btnLogin.innerText === "Login")
        btnLogin.innerText = "Logout";
    else
        btnLogin.innerText = "Login";
}

function removeElement(element){
    // Elimina el elemento.
    element.remove();
}

function showAlert(){
    // Presenta el mensaje de alerta.
    alert("Ninja was liked.");
}