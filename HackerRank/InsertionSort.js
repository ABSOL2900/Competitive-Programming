'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

function insertionSort1(n, arr) {
       // Write your code here

    let indexoflastnum=arr.length-1
   
   loop2: for(let i=arr.length-1;i>=0;i--)
    {
       
       let printarr=[]
       if(arr[i-1]>arr[i])
       {
        let temp=arr[i-1]
        arr[i-1]=arr[i]
        arr[i]=temp
        indexoflastnum-=1
      loop1: 
       for(let j=0;j<arr.length;j++)
       {
        if(arr[j]==arr[indexoflastnum])
        {
            printarr.push(arr[j+1])
        }
        else
        {
            printarr.push(arr[j])
        }
       }
       console.log(...printarr)

    }else
    {
        console.log(...arr)
        break loop2
    }

       
    }
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    insertionSort1(n, arr);
}
