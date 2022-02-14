function sum_checker (list, target) {
    for (let i = 0; i < list.length; i++) {
        let addedArray = [];
        for (let j = 0; j < i; j++) {
            addedArray[j] = list[j] + list[i];
            if (addedArray[j] == target) {
                //return String(list[i]).concat(' and ', String(list[j]), ' sum to ', String(target), '!');
                return true;
            }
        };
    };
    //return 'Nothing sums to '.concat(target, '... :(');
    return false;
};

let list = [10, 15, 3, 7];
let target = 17;

console.log(sum_checker(list, target));

// Use target - each input value and compare with the input values in a set to achieve O(N).