class BinaryTreeNode {
  constructor(key, value = key, parent = null) {
    this.key = key;
    this.value = value;
    this.parent = parent;
    this.left = null;
    this.right = null;
  }

  get isLeaf() {
    return this.left === null && this.right === null;
  }

  get hasChildren() {
    return !this.isLeaf;
  }
}

class BinaryTree {
  constructor(key, value = key) {
    this.root = new BinaryTreeNode(key, value);
  }

  *inOrderTraversal(node = this.root) {
    if (node.left) yield* this.inOrderTraversal(node.left);
    yield node;
    if (node.right) yield* this.inOrderTraversal(node.right);
  }

  *postOrderTraversal(node = this.root) {
    if (node.left) yield* this.postOrderTraversal(node.left);
    if (node.right) yield* this.postOrderTraversal(node.right);
    yield node;
  }

  *preOrderTraversal(node = this.root) {
    yield node;
    if (node.left) yield* this.preOrderTraversal(node.left);
    if (node.right) yield* this.preOrderTraversal(node.right);
  }

  insert(
    parentNodeKey,
    key,
    value = key,
    { left, right } = { left: true, right: true }
  ) {
    for (let node of this.preOrderTraversal()) {
      if (node.key === parentNodeKey) {
        const canInsertLeft = left && node.left === null;
        const canInsertRight = right && node.right === null;
        if (!canInsertLeft && !canInsertRight) return false;
        if (canInsertLeft) {
          node.left = new BinaryTreeNode(key, value, node);
          return true;
        }
        if (canInsertRight) {
          node.right = new BinaryTreeNode(key, value, node);
          return true;
        }
      }
    }
    return false;
  }

  remove(key) {
    for (let node of this.preOrderTraversal()) {
      if (node.left.key === key) {
        node.left = null;
        return true;
      }
      if (node.right.key === key) {
        node.right = null;
        return true;
      }
    }
    return false;
  }

  find(key) {
    for (let node of this.preOrderTraversal()) {
      if (node.key === key) return node;
    }
    return undefined;
  }
}

const testTree = new BinaryTree(1, 'AB');

testTree.insert(1, 11, 'AC');
testTree.insert(1, 12, 'BC');
testTree.insert(12, 121, 'BG', { right: true });

[...testTree.preOrderTraversal()].map(x => x.value);
// ['AB', 'AC', 'BC', 'BG']

[...testTree.inOrderTraversal()].map(x => x.value);
// ['AC', 'AB', 'BC', 'BG']

testTree.root.value;                // 'AB'
testTree.root.hasChildren;          // true

testTree.find(12).isLeaf;           // false
testTree.find(121).isLeaf;          // true
testTree.find(121).parent.value;    // 'BC'
testTree.find(12).left;             // null
testTree.find(12).right.value;      // 'BG'

testTree.remove(12);

[...testTree.postOrderTraversal()].map(x => x.value);
// ['AC', 'AB']

testTree.insert(1, 12, 'BC');
testTree.insert(12, 121, 'BG', { right: true });

function serialize(root) {
    if (root.isLeaf) {
        return root.value.concat(' # # ');
    } if (root.left === null) {
          return root.value.concat(' # ', serialize(root.right));
    } if (root.right === null) {
        return root.value.concat(serialize(root.left), ' # ');
    } else {
        return root.value.concat(' ', serialize(root.left), serialize(root.right));
    }
}

//console.log(serialize(testTree.root));

function deserialize(inputString) {
  inputArray = []
  while (inputString != '') {
    inputArray.push(inputString.substr(0, inputString.indexOf(' ')));
    inputString = inputString.substr(inputString.indexOf(' ') + 1);
  }
  return deserializeHelper(inputArray)
}

function deserializeHelper(inputArray) {
  for (let i = 0; i < inputArray.length - 1; i++) {
    // Need to add some way to keep track of where I am in the tree?
    if (inputArray[i] === '#' & (inputArray[i - 1] === '#' || inputArray[i + 1] === '#')) {
      // Leaf (next one is on the right)
    } if (inputArray[i] === '#') {
      // Single branch (next one is also on the right?)
    } else {
      // Two branches (next one is on the left)
    }
  }
}

let inputString = 'AB AC # # BC # BG # # '

let inputArray = ['AB', 'AC', '#', '#', 'BC', '#',  'BG', '#', '#']

console.log(deserializeHelper(inputArray));

// Probably better to do this in Python or another object-based language.

// https://www.dailycodingproblem.com/solution/3?token=f6d7400607a97bc1fb402e1bdc2158940c393e37ef06209d938abf2568b23913ec2333bf