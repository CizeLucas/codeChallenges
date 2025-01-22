/*
* Subtract the Nth smallest number from de right list with the Nth smallest number from the right list.
* sum up all those values
* 
* 1) Read the values from file
* 2) Separate the right and left lists into two distinct arrays
* 3) Order those arrays in a ascendent form
* 4) subtract them and add all those values into a another array
* 5) Sum all those values
*/

import * as fs from 'fs';
import { exit, listeners } from 'process';
import * as readline from 'readline';

// Variable for calculating Part ONE or Part TWO of the challenge
const isPartOne = false;

// Create a readable stream from the file
const fileStream = fs.createReadStream('input.txt');

// Use readline to create an interface for reading the file line by line
const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity // Recognizes all different kinds of newline formats (Windows, Unix, etc.)
});

let leftValues: number[] = [];
let rightValues: number[] = [];
let lines: string[] = [];


rl.on("line", (line) => {
    lines = line.split("   ");
    leftValues.push(Number(lines[0]));
    rightValues.push(Number(lines[1]));
});

// Handle end of file
rl.on('close', () => {
    let finalResult = 0;
    if(isPartOne) {
        // Part One
        console.log('Finished reading the file. \nCalculating the results...');
        console.log("Showing the first 10 results:");
        leftValues.sort((a, b) => a - b);
        rightValues.sort((a, b) => a - b);

        let numberDistance: number[] = [];
        
        for(let i=0; i<leftValues.length; i++) {
            numberDistance.push(Math.abs(leftValues[i] - rightValues[i]));
            if(i < 10)
                console.log(`${leftValues[i]} - ${rightValues[i]} = ${numberDistance[i]}`)
            finalResult += numberDistance[i];
        }
    } else {
        // Part Two
        let similarityScoreTuple: [number, number][] = [];

        for(let i=0; i<leftValues.length; i++) {
            
            if(!(leftValues[i] == leftValues[i+1] && i!=leftValues.length)) {
                let numberOfAppearances = 0;
                rightValues.forEach((number) => {
                    if(number == leftValues[i])
                        numberOfAppearances++;
                });
                similarityScoreTuple.push([leftValues[i], numberOfAppearances])
            }  
        }

        similarityScoreTuple.forEach( ([leftValue, appearances]) => {
            finalResult += leftValue * appearances;
        })
    }
    console.log(finalResult)
});

