# CILAssembler
A quick and dirty CIL assembler written in python in about 30 minutes


## General Usage
Run it and enter any CIL instruction based off https://en.wikipedia.org/wiki/List_of_CIL_instructions
Press enter without entering anything to assemble. If you want pretty/nice printing input the "instruction" `nice_print`.

## Usage as a library
There's two core functions which can be used. `Assemble` and `GetAssembleInstruction`. `Assemble` takes a chunk of instructions seperated with a new line and prints out the assembly. It has two arguments with the second being optional. The first argument is the instructions and the second is "nice printing".

`GetAssembleInstruction` takes only 1 argument which is a single instruction. It parses it and returns it's bytecode.

## Dependencies
Only `struct` is required.

### Without Nice Print
![Without Nice Printing](https://i.imgur.com/RHLX4cw.png)

### With Nice Print
![With Nice Printing](https://i.imgur.com/FTBmNy1.png)
