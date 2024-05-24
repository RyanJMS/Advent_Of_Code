import fs from "fs";

const input = fs.readFileSync("./day2_input.txt", "utf-8").split("\n");

const dimensions = input.map((i) => {
  let sorted = i
    .replace("\r", "")
    .split("x")
    .sort((a, b) => Number(a) - Number(b));

  return (
    Number(sorted[0]) * 2 +
    Number(sorted[1]) * 2 +
    Number(sorted[0]) * Number(sorted[1]) * Number(sorted[2])
  );
});

dimensions.pop();

const perim_dim = input.map((i) => {
  let sorted = i
    .replace("\r", "")
    .split("x")
    .sort((a, b) => Number(a) - Number(b));

  return (
    Number(sorted[0]) * Number(sorted[1]) * 2 +
    Number(sorted[0]) * Number(sorted[2]) * 2 +
    Number(sorted[1]) * Number(sorted[2]) * 2 +
    Number(sorted[0]) * Number(sorted[1])
  );
});

perim_dim.pop();

const sum = dimensions.reduce((curr, prev) => curr + prev, 0);

const perim_sum = perim_dim.reduce((curr, prev) => curr + prev, 0);

// console.log(sum);

// console.log(perim_sum);
