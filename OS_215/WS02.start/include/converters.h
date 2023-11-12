/**** converters.h ****/

#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>


/* Nb of converter pcs */
#define NB_CONVERTERS 5

/* Identifier for the converter in euros */
#define EUR_CONV 0
/* Identifier for the converter in pounds sterling */
#define GBP_CONV 1 
/* Identifier for the converter in US dollars */
#define USD_CONV 2 
/* Identifier for the converter in japanese yen */
#define JPY_CONV 3 
/* Identifier for the converter in chinese yuan */
#define CNY_CONV 4 

/* Conversion rate euro */
#define EUR 1			
/* Conversion rate pound sterling */
#define GBP 0.8388
/* Conversion rate US dollar */
#define USD 1.1255
/* Conversion rate yen */
#define JPY 114.096
/* Conversion rate yuan */
#define CNY 7.4986


/* Converts from a currency to another.
	input_currency :	currency to convert from
	target_currency :	currency to convert to
	input_amount :		amount to convert */
double convert(char* input_currency, char* target_currency, double input_amount);


/* Determines a currency string identifier, given its integer identifier */
char* determine_currency(int curr_nb);

/* Displays the result of a conversion */
void display_result(int target_currency, double conversion_result);
