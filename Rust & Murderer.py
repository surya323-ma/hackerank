Detective Rust is investigating a homicide and he wants to chase down the murderer. The murderer knows he would definitely get caught if he takes the main roads for fleeing, so he uses the village roads (or side lanes) for running away from the crime scene.
Rust knows that the murderer will take village roads and he wants to chase him down. He is observing the city map, but it doesn't show the village roads (or side lanes) on it and shows only the main roads.
The map of the city is a graph consisting  nodes (labeled  to ) where a specific given node  represents the current position of Rust and the rest of the nodes denote other places in the city, and an edge between two nodes is a main road between two places in the city. It can be suitably assumed that an edge that doesn't exist/isn't shown on the map is a village road (side lane). That means, there is a village road between two nodes  and  iff(if and only if) there is no city road between them.
In this problem, distance is calculated as number of village roads (side lanes) between any two places in the city.
Rust wants to calculate the shortest distance from his position (Node ) to all the other places in the city if he travels only using the village roads (side lanes).
Note: The graph/map of the city is ensured to be a sparse graph.
Input Format
The first line contains , denoting the number of test cases.  testcases follow.
First line of each test case has two integers , denoting the number of cities in the map and , denoting the number of roads in the map.
The next  lines each consist of two space-separated integers  and  denoting a main road between city  and city . The last line has an integer , denoting the current position of Rust.


#Javascript
'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the rustMurdered function below.
 */
function rustMurderer(n, graph, s) {
    const d = Array(n + 1);
    const sv = new Set();
    for (let i = 1; i <= n; i++) {
        d[i] = Number.MAX_SAFE_INTEGER;
        sv.add(i);
    }

    const stack = [];
    stack.size = 0;

    push(stack, s);
    d[s] = 0;
    sv.delete(s);

    while (stack.size > 0) {
        const v = pop(stack);
        const edges = graph[v];

        for (let i of sv) {
            if (!edges[i] && d[i] > d[v]) {
                d[i] = d[v] + 1;
                push(stack, i);
                sv.delete(i);
            }
        }
    }

    return d.filter((v, i) => !(i === 0 || i === s));
}

function pop(stack) {
    return stack[--stack.size];
}

function push(stack, value) {
    stack[stack.size++] = value;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const nm = readLine().split(' ');

        const n = parseInt(nm[0], 10);

        const m = parseInt(nm[1], 10);

        let graph = Array(n + 1);

        for (let i = 1; i <= n; i++) {
            graph[i] = {};
        }

        for (let roadsRowItr = 0; roadsRowItr < m; roadsRowItr++) {
            const edge = readLine().split(' ').map(roadsTemp => parseInt(roadsTemp, 10));

            graph[edge[0]][edge[1]] = true;
            graph[edge[1]][edge[0]] = true;
        }

        const s = parseInt(readLine(), 10);

        let result = rustMurderer(n, graph, s);

        ws.write(result.join(" ") + "\n");
    }

    ws.end();
}
