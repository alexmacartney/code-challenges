function excluding_summer (list) {
    let outputList = [];
    for (let i = 0; i < list.length; i++) {
        outputList[i] = 1;
        for (let j = 0; j < list.length; j++) {
            if (j != i) {
                outputList[i] *= list[j];
            }
        };
    };
    return outputList;
};

let list = [1, 2, 3, 4, 5];

console.log(excluding_summer(list));

list = [3, 2, 1];

console.log(excluding_summer(list));