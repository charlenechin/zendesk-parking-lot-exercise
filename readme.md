# Automated Valet Car Parking Backend Exercise

## Prerequisites

*Python 3.7

## Assumptions

* no special characters in input file - args in each line will always be delimited by " ", i.e. not implemeting sanitzing of inputs
* no invalid timestamps in input file - timestamp will always be in the correct format (unix timestamp), not implementing timestamp validations
* the first line of the file will always be 2 digits delimited by a space, i.e. not handlings invalid literal errors or additional inputs
* subsequent lines will follow the same sequence or format for "enter" and "exit" events - e.g. will not be expecting "Enter car 1613541902 SGF9283P" instead of "Enter car SGF9283P 1613541902"
* exit timestamp will not < enter timestamp - throwing exception for now, car will be stuck in carpark. Perhaps implement a maximum fee in the future?
* input file will not >= 4gb / too large, i.e. not accounting for and/or handling os errors

## Project Structure

```bash
.
├── data
│   └── test_data.txt <------------------- main.py file will take test input from this file in make command
├── main.py <----------------------------- main entry point
├── Makefile
├── Pipfile
├── readme.md
├── src <---------------------------------- project source code folder 
│   ├── constants.py <--------------------- used to keep predefined constants, i.e. vehicle name, parking fees
│   ├── handler.py <----------------------- cached object to handle Enter, Exit events, init of parking lot
│   └── models
│       ├── parking_lot.py <--------------- holds parking lots objects to handle lot availability and fees calculations
│       └── vehicle.py
└── tests <-------------------------------- unit tests here
    ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   └── test_parking_lot.py
    └── test_handler.py

```

## Future improvements

* the current implemenation will always search from index 0 when finding the lowest-numbered available lot
* this is a potential bottleneck if the parking lot has too many lots
* implementing priority queue in the `ParkingLot` object in `src/models/parking_lot.py` could alleviate this problem

## How To Run

### Main Valet Parking code

* replace test data in the file `data/test_data.txt`

```bash
# execute main.py for test file `data/test_data.txt`
$ make main
# alternatively, you can execute the main.py file with another filepath input
$ python main.py -file <path-to-file>
```

* you should then see the output on the console

### Unit Tests

``` bash
# execute unit tests
$ make tests
```
