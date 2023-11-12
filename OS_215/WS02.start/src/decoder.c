/**** decoder.c ****/

#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <decoder.h>
// I assume we are required to write decoder.h


#define _XOPEN_SOURCE 700


int magicsq[3][3] = {{4, -1, 8}, {-1, -1, -1}, {2, -1, 6}};


int check() {
	int i, j, sums[8];
	for (i = 0; i < 8; i++) 
		sums[i] = 0;
	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			sums[i] += magicsq[i][j];
			sums[i+3] += magicsq[j][i];
			if (i == j) sums[6] += magicsq[i][j];
			if ((i+j) == 2) sums[7] += magicsq[i][j];
		}
	}
	int result = 1;
	i = 1;
	while ((i < 8) && (result == 1)) {
		if (sums[0] != sums[i])
			result = 0;
		i++;
	}
	return result;
}


void display() {
	int i, j;
	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++)
			printf("  %d", magicsq[i][j]);
		printf("\n");
	}
	printf("\n");
}


// int solve(int x) {
// 	/* CODE THAT EVERY CHILD PROCESS EXECUTES */

// 	// Analytic solution (ChatGPT)

//     // Set the value of magic square at specific positions
//     magicsq[0][1] = x;

//     // Calculate the sum of the first row
//     int sum = magicsq[0][0] + magicsq[0][1] + magicsq[0][2];

//     // Calculate values of other positions based on the sum
//     magicsq[2][1] = sum - magicsq[2][0] - magicsq[2][2];
//     magicsq[1][0] = sum - magicsq[0][0] - magicsq[2][0];
//     magicsq[1][1] = sum - magicsq[0][1] - magicsq[2][1];
//     magicsq[1][2] = sum - magicsq[0][2] - magicsq[2][2];

//     // Check if any position has a negative value or a value greater than 9
//     if ((magicsq[2][1]<0) || (magicsq[1][1]<0) || (magicsq[1][0]<0) || (magicsq[1][2]<0) ||
//         (magicsq[2][1]>9) || (magicsq[1][1]>9) || (magicsq[1][0]>9) || (magicsq[1][2]>9)) {
//         return -1;
//     }

//     // Check if the solution is valid
//     if (check()){
//         printf("Solution:\n");
//         display();
//     }

//     // Return 1 if successful
//     return 1;
// }


int solve(int a) {
	/* CODE THAT EVERY CHILD PROCESS EXECUTES */

	// BRUTE FORCE SOLUTION
	// The key steps are:
	// 		Loop through all possible values of b, c, d, e from 0 to 9
	// 		Set the magic square entries based on a, b, c, d, e
	// 		Check if resulting square is magic with check()
	// 		If magic, display the solution
	// This brute forces all combinations of b,c,d,e for the given 'a' value that is passed to solve().

  	int b, c, d, e;

  	for (b=0; b<10; b++) {
    	for (c=0; c<10; c++) {
      		for (d=0; d<10; d++) {
        		for (e=0; e<10; e++) {
          
					magicsq[0][1] = a;
					magicsq[1][0] = b; 
					magicsq[1][1] = c;
					magicsq[1][2] = d;
					magicsq[2][1] = e;

					if (check()) {
						printf("Decoder Solution:\n");
						display();
					}

        		}
      		}
    	}
  	}

  	return 0;

}

int main(int argc, char **argv)
{	
	/* PARENT PROCESS */

	pid_t pid;
	int i;

	for (i = 0; i < 10; i++) {
		pid = fork();
		if (pid == 0) {
			// Child process
			solve(i); 
			exit(0);
		}
	}

	// Parent waits for children
	for(i = 0; i < 10; i++) {
		wait(NULL);
	}

	return 0;
}

