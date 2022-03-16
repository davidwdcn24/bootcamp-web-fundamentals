function alwaysHungry(arr){
    let esComida = false;
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        esComida = arr[i] === "comida";
        if (esComida) {
            result.push("delicioso");
        }
    }

    if (result.length === 0)
        result.push("Tengo hambre");

    console.log("método: alwaysHungry", result);
}
alwaysHungry([3.14, "comida", "pastel", true, "comida"]);
alwaysHungry([4, 1, 5, 7, 2]);

function highPass(arr, cutoff){
    var filteredArr = [];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]);
        }
    }

    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log("método: highPass", result);

function betterThanAverage(arr) {
    var sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }

    // calcula el promedio
    var count = 0;
    var promedio = sum / arr.length;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > promedio)
            count++;
    }

    // cuenmta cuánmtas variables son mayores que el promedio
    return count;
}
result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log("método: betterThanAverage", result);

function reverse(arr) {
    let result = [];
    
    for (let i = arr.length - 1; i >= 0; i--) {
        result.push(arr[i]);
    }

    return result;
}
result = reverse(["a", "b", "c", "d", "e"]);
console.log("método: reverse", result);

function fibonacciArray(n) {
    // [0, 1] son los valores inciales del arreglos para calcular el resto
    var fibArr = [0, 1];

    for (let i = 2; i < n; i++) {
        fibArr.push(fibArr[fibArr.length - 1] + fibArr[fibArr.length - 2]);
    }

    // tu código aquí
    return fibArr;
}
result = fibonacciArray(10);
console.log("método: fibonacciArray", result);