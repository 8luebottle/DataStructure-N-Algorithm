// Implement Stack in JavaScript

class Stack {
  constructor(){
    this.stack = [];
  }

  push(item) {
    return this.stack.push(item);
  }

  pop() {
    return this.stack.pop();
  }

  peek(){
    return this.stack[this.length - 1];
  }

  get length(){
    return this.stack.length;
  }

  isEmpty() {
    return this.length === 0;
  }
}

// Testing
let testStack = new Stack();
testStack.push("DataStructure");
testStack.push("And");
testStack.push("Algorithm");
console.log(testStack);
console.log(testStack.length);
console.log(testStack.peek());
testStack.pop();
console.log(testStack.length);
console.log(testStack.isEmpty());
console.log(testStack);