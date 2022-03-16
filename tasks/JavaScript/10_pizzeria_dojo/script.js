var sandwich = {
    pan:    "masa madre",
    proteína:  "asado",
    queso:   "queso suizo lacey",
    salsas: ["lechuga romana", "tomates reliquia", "salsa de rábano"]
};
    
// console.log(sandwich);

function sandwichFactory(pan, proteína, queso, salsas) {
    var sandwich = {};
    sandwich.pan = pan;
    sandwich.proteína = proteína;
    sandwich.queso = queso;
    sandwich.salsas = salsas;
    return sandwich;
}
    
// var s1 = sandwichFactory("trigo", "pavo", "provolone", ["mostaza", "cebolla frita", "rúcula"]);
// console.log(s1);

function pizzaOven(tipoCorteza, tipoSalsa, quesos, salsas){
    var pizza = {};
    pizza.tipoCorteza = tipoCorteza;
    pizza.tipoSalsa = tipoSalsa;
    pizza.quesos = quesos;
    pizza.salsas = salsas;
    return pizza;
}
var pizzaUno = pizzaOven("estilo Chicago", "tradicional", ["mozzarella"], ["pepperoni", "salchicha"]);
var pizzaDos = pizzaOven("lanzada a mano" , "marinara" , ["mozzarella", "feta"], ["champiñones", "aceitunas", "cebollas"]);

console.log("pizzaUno: ", pizzaUno);
console.log("pizzaDos: ", pizzaDos);

var pizzaTres = pizzaOven("normal", "tradicional", ["mozzarella", "holandes"], ["jamón", "piña"]);
var pizzaCuatro = pizzaOven("normal" , "marinara" , ["mozzarella", "parmesano"], ["carne", "jamón", "pepperoni", "salchicha italiana"]);

console.log("pizzaTres: ", pizzaTres);
console.log("pizzaCuatro: ", pizzaCuatro);