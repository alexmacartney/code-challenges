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

// Use two for loops to multiply the values before and after each index.
// Use a final for loop to combine the above two outputs.

// https://www.dailycodingproblem.com/solution/2?token=f88fadaf712da1817838001dcb88c72a34df728846a45bdd0876a1c171e9be60a0c157ad