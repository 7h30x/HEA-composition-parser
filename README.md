# alloy-mechanical-properties-parser
A parser to extract alloy mechanical properties information from a .csv file. 

### Parser Functions

- normalizes molar ratios
- reads implicit '1' molar ratio

### Input Format 

- requires a single row .csv file with alloy chemical compositions
- include a header row titled "Composition"


### Output Format

- a .csv file containing the same number of rows as valid rows in the .csv
- columns of the output file correspond to one element for a total of *n* elements
> e.g. [ 0, 0.5, 0.2,  ... , 0.1 ]
- a header column of the element symbols is included 
> e.g. ["Cu", "Cr", "Al", ... , "Fe" ]


### Use Instructions

Put the input file in the `/assets` directory and run the following in terminal on the project root directory:
``` bash
python3 main.py '/assets/[filename].csv' ','
```
