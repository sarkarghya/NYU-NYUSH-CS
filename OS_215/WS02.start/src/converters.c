/**** converters.c ****/

#include <string.h>
#include <converters.h>

#define _XOPEN_SOURCE 700


/* Converts from any to EUR */
double convertfrom(char* input_currency, double input_amount) {
	if (strcmp(input_currency, "GBP") == 0)
		return (input_amount / GBP);
	else if (strcmp(input_currency, "USD") == 0)
		return (input_amount / USD);
	else if (strcmp(input_currency, "JPY") == 0)
		return (input_amount / JPY);
	else if (strcmp(input_currency, "CNY") == 0)
		return (input_amount / CNY);
	else if (strcmp(input_currency, "EUR") == 0)
		return input_amount;
	else {
		perror("Unknown currency");
		exit(1);
	}
}


/* Converts from EUR to any */
double convertto(char* target_currency, double input_amount) {
	if (strcmp(target_currency, "GBP") == 0)
		return (input_amount * GBP);
	else if (strcmp(target_currency, "USD") == 0)
		return (input_amount * USD);
	else if (strcmp(target_currency, "JPY") == 0)
		return (input_amount * JPY);
	else if (strcmp(target_currency, "CNY") == 0)
		return (input_amount * CNY);
	else if (strcmp(target_currency, "EUR") == 0)
		return input_amount;
	else {
		perror("Unknown currency");
		exit(1);
	}
}


/* Converts from one currency to another.
	input_currency :	currency to convert from
	target_currency :	currency to convert to
	input_amount :		amount to convert */
double convert(char* input_currency, char* target_currency, double input_amount) {
	return convertto(target_currency, convertfrom(input_currency, input_amount));
}


/* Determines a currency string identifier, given its integer identifier */
char* determine_currency(int curr_nb) {
	switch(curr_nb) {
		case EUR_CONV: return "EUR";
		case GBP_CONV: return "GBP";
		case USD_CONV: return "USD";
		case JPY_CONV: return "JPY";
		case CNY_CONV: return "CNY";
		default: perror("Unknown currency"); exit(1);
	}
}


void display_result(int target_currency, double conversion_result) {
    printf("\t %s %.3f\n", determine_currency(target_currency), conversion_result);
}

/*
int main(int argc, char **argv)
{
	int i;
	char src_currency[4], target_currency[4];
	float src_amount;
	
	strcpy(src_currency, "JPY");
	strcpy(target_currency, "EUR");
	src_amount = 12.0;
	printf("test 1> %d %.3f -> %d =  %.3f\n", src_currency, 
				src_amount, 
				target_currency, 
				convert(src_currency, target_currency, src_amount));

	return 0;
}
*/