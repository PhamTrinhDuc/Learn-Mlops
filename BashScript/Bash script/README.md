# How-to Guide
## Basic Script
In this example, you will learn all the basics of bash scripting,
to run it, you can use the following commands:
```bash
cd scripts && bash basic_script.sh
```
OR
```bash
cd scripts && chmod + x basic_script.sh && ./basic_script.sh
```

## Install Me

This script is to simulate the installation of a program, in which you need
to type y or n to confirm the installation.

Use the similar command as the above to run it.

## Newline Watcher
This example echos the new appended line to the terminal.
First, open a terminal window, and run the following command
```bash
cd scripts && bash newline_watcher.sh ../data/data2_copy.csv
```
, then open a new terminal window, and run the following command
```bash
cd scripts && echo '4.9,3.1,1.5,.1,"Setosa"' >> ../data/data2_copy.csv
```
Remember, `>>` is used to append a new line to the data, while `>` is used for overwrite.

## Calculate frequencies
This example calculates the frequencies of flower species in 2 csv files.
Please run the following command to calculate the frequencies:
```bash
cd scripts && bash calculate_frequencies.sh ../data
```

## Makefile
```bash
make build
make deploy
make ci
```