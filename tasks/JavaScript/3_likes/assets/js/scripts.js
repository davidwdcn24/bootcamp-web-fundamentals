let user_likes = {
    someUser: {
        name: "Some user",
        counter: 3
    },
    neil: {
        name: "Neil M",
        counter: 9
    },
    nichole: {
        name: "Nichole K",
        counter: 12
    },
    jim: {
        name: "Jim R",
        counter: 9
    }
};

function addLikesPartI(idContainer){
    // Agrega un like
    user_likes[idContainer].counter++;

    // Imprime el contador
    let spnLike = document.querySelector("#" + idContainer);
    spnLike.innerText = user_likes[idContainer].counter + " like(s)";
}