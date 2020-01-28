# TSP-Genetic-Algo
Simple TSP solution via genetic algorithm

## Introduction
Simple implementation of using a genetic algorithm to attempt to solve the Travelling Salesman Problem.

## Installation
```
git clone https://github.com/lawruixi/TSP-Genetic-Algo
```

## Usage
Two files are provided, tsp.py and tsp_traditional.py. tsp_traditional is a simple brute-force search of the entire list to find the shortest path. As such it may take... _some_ time to run for higher number of cities. tsp.py is an implementation of a genetic algorithm.

tsp.py randomly generates cities and uses genetic algo to attempt to find the best route.
```
python3 tsp.py
```

Since the output may be quite lengthy, you may want to redirect the output to a text file you can analyze at your own leisure:
```
python3 tsp.py > output.txt
```

## Future Work
- Improve accuracy of genetic algorithm.
- Read cities from file instead of randomly generating all the time.

## Contributing
If you would like to contribute, sure. Pull requests are welcome ;)


