function changeNameProfile(){
    let userName = document.querySelector("#user_name");

    // Obtiene el nombre actual.
    if(userName.innerText === "Jane Doe")
        userName.innerText = "Coding Dojo";
    else 
        userName.innerText = "Jane Doe";
}

function removeConnectionRequest(element){
    // Obtiene el elemento que se va a eliminar
    let connection = element.parentElement.parentElement;

    if(connection !== null && connection !== undefined){
        connection.remove();

        // Obtiene el número de conexiones.
        var bdgConnection = document.querySelector("#bdgConnection");
        let contador = parseInt(bdgConnection.innerText);

        // Actualiza el contador.
        contador--;
        bdgConnection.innerText = contador;
    }
}

function aceptConnectionRequest(element){
    // Obtiene la opción de la lista.
    let item_list = element.parentElement.parentElement.querySelector(".imagen-requests");

    // Obtiene la imagen 
    let image = item_list.getElementsByTagName("img")[0];
    let span = item_list.getElementsByTagName("span")[0];
    
    // Agrega a tus conexiones.
    let connection = "<li>" + 
                        "<div class='imagen-connections'>" + 
                            "<img src='" + image.src + "' />" +
                            "<span>" + span.innerText + "</span>" + 
                        "</div>" + 
                    "</li>";
    let list = document.querySelector("#lstYourConnections");
    /*

    element.insertAdjacentHTML(position, text);

    position:
    The position relative to the element. Can be one of the following:

    'beforebegin': Before the element;
    'afterbegin': Inside the element, before its first child;
    'beforeend': Inside the element, after its last child;
    'afterend': After the element.

     */
    list.insertAdjacentHTML("beforeend", connection);

    // Elimina la conexión
    removeConnectionRequest(element);
}