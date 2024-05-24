const fs = require("fs");

const input = fs.readFileSync("./day1_input.txt", "utf-8");

let floors = 0;

for (let i = 0; i <= input.length; i++) {
  if (floors < 0) {
    console.log(i);
    break;
  }
  if (input[i] === "(") {
    floors += 1;
  }
  if (input[i] === ")") {
    floors -= 1;
  }
}

console.log(floors);
