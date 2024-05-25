Name = Arghya Sarkar
NetID = abs9425

Compilation:

- A Makefile is provided to compile the programs.
- Edit the CFLAGS variable to specify include directories and libraries.
- Run `make` to build all programs.
- Or run `make build_<name>` to build a specific program.
- Object files will be in obj/ and executables in bin/.

Running Programs: 

- Run `make run_Q1` to run the multi-upper program on sample text files.
- Run `make run_Q2` to run the multi-upper-ftd program. 
- Run `make run_Q3` to run the bounded-buffer program.

Cleaning:

- Run `make clean` to delete compiled files and output text files. 

Notes:

- The Makefile builds the programs separately.
- CFLAGS contains common flags needed for compiling.
- Object files are placed in the obj/ directory.
- Executables are placed in the bin/ directory.
- Sample text files are provided in text/
- Output files will be in text/ with .UPPER.txt suffix.

Comments:
- For Q3 I consider that a total of the `NC` consumer consumes `NVAL` values cumulatively.