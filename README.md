# EDA Final Project

2020 CAD Contest ProblemA: X-value Equivalence Checking

### What's in this folder
```
final_project/
├── README.md               --- intructions of this project
├── presentation.pdf        --- our slides
├── report.pdf              --- our report
└── src/                    --- our code
    ├── testcases/          --- test cases
    └── main/               --- main code
```

### Dependencies
* python3
* [yosys](https://github.com/YosysHQ/yosys): Yosys Open SYnthesis Suite
* [abc](https://github.com/berkeley-abc/abc): System for Sequential Logic Synthesis and Formal Verification

### Instructions

1. Install yosys.
2. Install abc.
3. Download the zip file and unzip it.
4. Go to the working directory
```
cd final_project/src/
```
5. Run the shell script.
```
sh run.sh <test_case_dir>
```
6. The result will be `UNSATISFIABLE` for equivalent cases and `SATISFIABLE` for non-equivalent cases.

