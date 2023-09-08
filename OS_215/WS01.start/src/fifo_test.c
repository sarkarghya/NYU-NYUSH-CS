#include <fifo.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	
	char* mywords[4] = {"The Force", "is", "strong", "within this Jedi"};
	int i;
	int nb;
	
	init_queue();
	
	for(i = 0; i < 4; i++)
		queue(mywords[i]);
	
	nb = size();
	
	printf("The size of the queue is %d\n", nb);
	
	for(i = 0; i < nb; i++)
		printf("%s \n", (char*)dequeue());
	
	return EXIT_SUCCESS;
}