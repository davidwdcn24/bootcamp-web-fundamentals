function getFizzbuzz(initial, end){
    for(let i = initial; i <= end; i++){
        let esMultiploTres = i % 3 === 0;
        let esMultiploCinco = i % 5 === 0;

        // Imprime el valor
        if(esMultiploTres && !esMultiploCinco)
            console.log("Fizz");
        else if (!esMultiploTres && esMultiploCinco)
            console.log("Buzz");
        else if (esMultiploTres && esMultiploCinco)
            console.log("FizzBuzz");
        else
            console.log(i);
    }
}

getFizzbuzz(1, 100);