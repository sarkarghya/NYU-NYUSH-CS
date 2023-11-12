/**** multi-converter.c ****/

#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <converters.h>


#define _XOPEN_SOURCE 700


int main(int argc, char **argv) {
    int i;
    pid_t pid;
    // List of currency codes
    char cur_list[][4] = {"EUR", "GBP", "USD", "JPY", "CNY"};

    // Source and target currency codes
    char src_currency[4] = "";
    char target_currency[4] = "";

    // Copy command line arguments to variables
    strcpy(src_currency, argv[1]);
    double src_amount = atof(argv[2]);

    // Print source currency and amount
    printf("Conversion for: %s  %.3f\n", src_currency, src_amount);

    for (i = 0; i < 5; i++) {
        if ((pid = fork()) == 0) {
            // Child process
            strcpy(target_currency, cur_list[i]);
            printf("\t %s  %.3f\n",
                   target_currency,
                   convert(src_currency, target_currency, src_amount));
            exit(1); // Exit child process
        }
    }

    // Wait for all child processes to finish
    while (i != 0) {
        i--;
        wait(NULL);
    }

    // Print end message
    printf("End of conversion\n");
    return EXIT_SUCCESS;
}
