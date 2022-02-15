function first_missing_positive_integer(inputArray) {
    let set = new Set(inputArray);
    i = 1;
    while (set.has(i)) {
        i += 1
    }
    return i
}

let testArray = [2, 3, 6, 0, -1, -3, 1]

console.log(first_missing_positive_integer(testArray))

// Not sufficient as runs on O(N) space.

// https://www.dailycodingproblem.com/solution/4?token=06627484f7950319a61b4cb46c91b937fd1cb619b818cddb3ba961cf895a30072214f76a