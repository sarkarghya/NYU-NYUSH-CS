/*
 * Gift Card Reading Application
 * Original Author: Shoddycorp's Cut-Rate Contracting
 * Comments added by: Justin Cappos (JAC) and Brendan Dolan-Gavitt (BDG)
 * Maintainer:
 * Date: 8 July 2020
 */


#include "giftcard.h"

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>

#define MAX_GIFT_CARD_SIZE 4096
#define MAX_RECORDS 1000
#define MESSAGE_SIZE 32
#define PROGRAM_SIZE 256
#define MSG_BUFFER_SIZE 32

// .,~==== interpreter for THX-1138 assembly ====~,.
//
// This is an emulated version of a microcontroller with
// 16 registers, one flag (the zero flag), and display
// functionality. Programs can operate on the message
// buffer and use opcode 0x07 to update the display, so
// that animated greetings can be created.
void animate(char *msg, unsigned char *program) {
    unsigned char regs[16];
    char *mptr = msg; // TODO: how big is this buffer?
    if (mptr < msg || mptr >= msg + MSG_BUFFER_SIZE) {
        exit(1);
    }
    unsigned char *pc = program;
    int i = 0;
    int zf = 0;
    while (pc < program+256) {
        unsigned char op, arg1, arg2;
        op = *pc;
        arg1 = *(pc+1);
        arg2 = *(pc+2);
        switch (*pc) {
            case 0x00:
                break;
            case 0x01:
                regs[arg1] = *mptr;
                break;
            case 0x02:
                *mptr = regs[arg1];
                break;
            case 0x03:
                mptr += (char)arg1;
                break;
            case 0x04:
                regs[arg2] = arg1;
                break;
            case 0x05:
                regs[arg1] ^= regs[arg2];
                zf = !regs[arg1];
                break;
            case 0x06:
                regs[arg1] += regs[arg2];
                zf = !regs[arg1];
                break;
            case 0x07:
                puts(msg);
                break;
            case 0x08:
                goto done;
            case 0x09:
                pc += (char)arg1;
                break;
            case 0x10:
                if (zf) pc += (char)arg1;
                break;
        }
        pc+=3;
#ifndef FUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION
        // Slow down animation to make it more visible (disabled if fuzzing)
        usleep(5000);
#endif
    }
done:
    return;
}

int get_gift_card_value(struct this_gift_card *thisone) {
	struct gift_card_data *gcd_ptr;
	struct gift_card_record_data *gcrd_ptr;
	struct gift_card_amount_change *gcac_ptr;
	int ret_count = 0;

	gcd_ptr = thisone->gift_card_data;
	for(int i=0;i<gcd_ptr->number_of_gift_card_records; i++) {
  		gcrd_ptr = (struct gift_card_record_data *) gcd_ptr->gift_card_record_data[i];
		if (gcrd_ptr->type_of_record == 1) {
			gcac_ptr = gcrd_ptr->actual_record;
			ret_count += gcac_ptr->amount_added;
		}
	}
	return ret_count;
}

void print_gift_card_info(struct this_gift_card *thisone) {
	struct gift_card_data *gcd_ptr;
	struct gift_card_record_data *gcrd_ptr;
	struct gift_card_amount_change *gcac_ptr;
    struct gift_card_program *gcp_ptr;

	gcd_ptr = thisone->gift_card_data;
	printf("   Merchant ID: %32.32s\n",gcd_ptr->merchant_id);
	printf("   Customer ID: %32.32s\n",gcd_ptr->customer_id);
	printf("   Num records: %d\n",gcd_ptr->number_of_gift_card_records);
	for(int i=0;i<gcd_ptr->number_of_gift_card_records; i++) {
  		gcrd_ptr = (struct gift_card_record_data *) gcd_ptr->gift_card_record_data[i];
		if (gcrd_ptr->type_of_record == 1) {
			printf("      record_type: amount_change\n");
			gcac_ptr = gcrd_ptr->actual_record;
			printf("      amount_added: %d\n",gcac_ptr->amount_added);
			if (gcac_ptr->amount_added>0) {
				printf("      signature: %32.32s\n",gcac_ptr->actual_signature);
			}
		}
		else if (gcrd_ptr->type_of_record == 2) {
			printf("      record_type: message\n");
			printf("      message: %s\n",(char *)gcrd_ptr->actual_record);
		}
		else if (gcrd_ptr->type_of_record == 3) {
            gcp_ptr = gcrd_ptr->actual_record;
			printf("      record_type: animated message\n");
            // BDG: Hmm... is message guaranteed to be null-terminated?
            size_t msg_len = strnlen(gcp_ptr->message, MESSAGE_SIZE);
            if (strnlen(gcp_ptr->message, MESSAGE_SIZE) != (MESSAGE_SIZE - 1)) {
                fprintf(stderr, "Error: Message is not null-terminated (size: %zu)\n", msg_len);
                exit(1);
            }
            printf("      message: %s\n", gcp_ptr->message);
            printf("  [running embedded program]  \n");
            animate(gcp_ptr->message, gcp_ptr->program);
		}
	}
	printf("  Total value: %d\n\n",get_gift_card_value(thisone));
}

// Added to support web functionalities
void gift_card_json(struct this_gift_card *thisone) {
    struct gift_card_data *gcd_ptr;
    struct gift_card_record_data *gcrd_ptr;
    struct gift_card_amount_change *gcac_ptr;
    gcd_ptr = thisone->gift_card_data;
    printf("{\n");
    printf("  \"merchant_id\": \"%32.32s\",\n", gcd_ptr->merchant_id);
    printf("  \"customer_id\": \"%32.32s\",\n", gcd_ptr->customer_id);
    printf("  \"total_value\": %d,\n", get_gift_card_value(thisone));
    printf("  \"records\": [\n");
	for(int i=0;i<gcd_ptr->number_of_gift_card_records; i++) {
        gcrd_ptr = (struct gift_card_record_data *) gcd_ptr->gift_card_record_data[i];
        printf("    {\n");
        if (gcrd_ptr->type_of_record == 1) {
            printf("      \"record_type\": \"amount_change\",\n");
            gcac_ptr = gcrd_ptr->actual_record;
            printf("      \"amount_added\": %d,\n",gcac_ptr->amount_added);
            if (gcac_ptr->amount_added>0) {
                printf("      \"signature\": \"%32.32s\"\n",gcac_ptr->actual_signature);
            }
        }
        else if (gcrd_ptr->type_of_record == 2) {
			printf("      \"record_type\": \"message\",\n");
			printf("      \"message\": \"%s\"\n",(char *)gcrd_ptr->actual_record);
        }
        else if (gcrd_ptr->type_of_record == 3) {
            struct gift_card_program *gcp = gcrd_ptr->actual_record;
			printf("      \"record_type\": \"animated message\",\n");
			printf("      \"message\": \"%s\",\n",gcp->message);
            // programs are binary so we will hex for the json
            char *hexchars = "01234567890abcdef";
            char program_hex[512+1];
            program_hex[512] = '\0';
            int i;
            for(i = 0; i < 256; i++) {
                program_hex[i*2] = hexchars[((gcp->program[i] & 0xf0) >> 4)];
                program_hex[i*2+1] = hexchars[(gcp->program[i] & 0x0f)];
            }
			printf("      \"program\": \"%s\"\n",program_hex);
        }
        if (i < gcd_ptr->number_of_gift_card_records-1)
            printf("    },\n");
        else
            printf("    }\n");
    }
    printf("  ]\n");
    printf("}\n");
}


struct this_gift_card *gift_card_reader(FILE *input_fd) {

	struct this_gift_card *ret_val = malloc(sizeof(struct this_gift_card));

    void *optr;
	void *ptr;

	// Loop to do the whole file
	// while (!feof(input_fd)) {

		struct gift_card_data *gcd_ptr;
		/* JAC: Why aren't return types checked? */
		size_t elements_read = fread(&ret_val->num_bytes, 4,1, input_fd);
        if (elements_read != 1) {
            free(ret_val);
            if (feof(input_fd)) {
                fprintf(stderr, "Unexpected end of file\n");
            } else if (ferror(input_fd)) {
                perror("File read error");
            }
            exit(1);
        }

		// Make something the size of the rest and read it in
        if (ret_val->num_bytes > MAX_GIFT_CARD_SIZE) {
            fprintf(stderr, "Gift card size exceeds maximum\n");
            free(ret_val);
            exit(1);
        }
		ptr = malloc(ret_val->num_bytes);
        if (!ptr) {
            free(ret_val);
            exit(1);
        }
		fread(ptr, ret_val->num_bytes, 1, input_fd);

        optr = ptr-4;

        size_t remaining_bytes = ret_val->num_bytes;

		ret_val->gift_card_data = malloc(sizeof(struct gift_card_data));
        gcd_ptr = ret_val->gift_card_data;

        if (remaining_bytes < 64) {
            fprintf(stderr, "Insufficient data for merchant_id and customer_id\n");
            free(gcd_ptr);
            free(ret_val);
            exit(1);
        }
		gcd_ptr->merchant_id = ptr;
        if (remaining_bytes < 32) {
            fprintf(stderr, "Insufficient data\n");
            exit(1);
        }
		ptr += 32;
//		printf("VD: %d\n",(int)ptr - (int) gcd_ptr->merchant_id);
		gcd_ptr->customer_id = ptr;
        if (remaining_bytes < 32) {
            fprintf(stderr, "Insufficient data\n");
            exit(1);
        }
		ptr += 32;
        remaining_bytes -= 64;
		/* JAC: Something seems off here... */

        if (remaining_bytes < sizeof(uint32_t)) {
            fprintf(stderr, "Insufficient data for number_of_gift_card_records\n");
            free(gcd_ptr);
            free(ret_val);
            exit(1);
        }

		memcpy(&gcd_ptr->number_of_gift_card_records, ptr, sizeof(uint32_t));
        if (remaining_bytes < sizeof(uint32_t)) {
            fprintf(stderr, "Insufficient data\n");
            exit(1);
        }
        if (remaining_bytes < 32) {
            fprintf(stderr, "Insufficient data\n");
            exit(1);
        }
        ptr += sizeof(uint32_t);
        remaining_bytes -= sizeof(uint32_t);

        if (gcd_ptr->number_of_gift_card_records > MAX_RECORDS) {
            fprintf(stderr, "Invalid number of gift card records: %u\n", gcd_ptr->number_of_gift_card_records);
            free(ret_val->gift_card_data);
            free(ret_val);
            exit(1);
        }

		gcd_ptr->gift_card_record_data = (void *)malloc(gcd_ptr->number_of_gift_card_records*sizeof(void*));

        if (!gcd_ptr || gcd_ptr->number_of_gift_card_records > MAX_RECORDS) {
            fprintf(stderr, "Invalid number of gift card records: %u\n", gcd_ptr->number_of_gift_card_records);
            free(ret_val->gift_card_data);
            free(ret_val);
            exit(1);
        }

		// Now ptr points at the gift card record data
		for (int i=0; i < gcd_ptr->number_of_gift_card_records; i++){
			//printf("i: %d\n",i);
			struct gift_card_record_data *gcrd_ptr;
			gcrd_ptr = gcd_ptr->gift_card_record_data[i] = malloc(sizeof(struct gift_card_record_data));

            if (!gcrd_ptr) {
                fprintf(stderr, "Memory allocation failed\n");
                exit(1);
            }
			// struct gift_card_amount_change *gcac_ptr;

			// gcac_ptr = gcrd_ptr->actual_record = malloc(sizeof(struct gift_card_record_data));
            

			gcrd_ptr->record_size_in_bytes = *((unsigned int *)ptr);
            //printf("rec at %x, %d bytes\n", ptr - optr, gcrd_ptr->record_size_in_bytes);
            if (remaining_bytes < 4) {
                fprintf(stderr, "Insufficient data\n");
                exit(1);
            }
			ptr += 4;
			//printf("record_data: %d\n",gcrd_ptr->record_size_in_bytes);
			gcrd_ptr->type_of_record = *((unsigned int *)ptr);
            if (remaining_bytes < 4) {
                fprintf(stderr, "Insufficient data\n");
                exit(1);
            }
			ptr += 4;
            //printf("type of rec: %d\n", gcrd_ptr->type_of_record);
            remaining_bytes -= 8;

			// amount change
			if (gcrd_ptr->type_of_record == 1) {
                struct gift_card_amount_change *gcac_ptr = gcrd_ptr->actual_record = malloc(sizeof(struct gift_card_amount_change));
                if (!gcac_ptr) {
                    fprintf(stderr, "Memory allocation failed\n");
                    exit(1);
                }
                gcac_ptr->amount_added = *((int*) ptr);
                if (remaining_bytes < 4) {
                    fprintf(stderr, "Insufficient data\n");
                    exit(1);
                }
                ptr += 4;
                if (gcac_ptr->amount_added >= 0) {
                    gcac_ptr->actual_signature = ptr;
                    ptr += 32;
                    remaining_bytes -= 32;
                }
            } else if (gcrd_ptr->type_of_record == 2) {
                gcrd_ptr->actual_record = ptr;
                size_t msg_len = strnlen(ptr, 1024);
                if (remaining_bytes < msg_len + 1) {
                    fprintf(stderr, "Insufficient data\n");
                    exit(1);
                }
                ptr += msg_len + 1;
                remaining_bytes -= (msg_len + 1);
            }
            // BDG: gift cards cåan run code?? Might want to check this one carefully...
            // text animatino (BETA)
            else if (gcrd_ptr->type_of_record == 3) {
                struct gift_card_program *gcp_ptr;
                gcp_ptr = malloc(sizeof(struct gift_card_program));
                if (!gcp_ptr) {
                    fprintf(stderr, "Memory allocation failed for animated record\n");
                    exit(1);
                }

                gcp_ptr->message = malloc(MESSAGE_SIZE);
                if (!gcp_ptr->message) {
                    fprintf(stderr, "Memory allocation failed for message\n");
                    exit(1);
                }

                gcp_ptr->program = malloc(PROGRAM_SIZE);
                if (!gcp_ptr->program) {
                    fprintf(stderr, "Memory allocation failed for program\n");
                    free(gcp_ptr->message);
                    exit(1);
                }

                /* Initialize buffers */
                memset(gcp_ptr->message, 0, MESSAGE_SIZE);
                memset(gcp_ptr->program, 0, PROGRAM_SIZE);

                /* Copy message and validate */
                memcpy(gcp_ptr->message, ptr, 32);
                if (remaining_bytes < 32) {
                    fprintf(stderr, "Insufficient data\n");
                    exit(1);
                }
                ptr += 32;

                /* Throw an error if the message isn’t null terminated */
                if (memchr(gcp_ptr->message, '\0', MESSAGE_SIZE) == NULL) {
                    fprintf(stderr, "Error: animated message is not null terminated.\n");
                    exit(1);
                }

                /* Copy the program bytes */
                memcpy(gcp_ptr->program, ptr, PROGRAM_SIZE);
                if (remaining_bytes < 256) {
                    fprintf(stderr, "Insufficient data\n");
                    exit(1);
                }
                ptr += PROGRAM_SIZE;
                remaining_bytes -= (32 + 256);

                gcrd_ptr->actual_record = gcp_ptr;
            }


            if (gcrd_ptr->type_of_record > 3) {
                printf("unknown record type: %d\n", gcrd_ptr->type_of_record);
                exit(1);
            }
		// }
	}
	return ret_val;
}

struct this_gift_card *thisone;

int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "usage: %s <1|2> file.gft\n", argv[0]);
        fprintf(stderr, "  - Use 1 for text output, 2 for JSON output\n");
        return 1;
    }
	FILE *input_fd = fopen(argv[2],"r");
    if (!input_fd) {
        fprintf(stderr, "error opening file\n");
        return 1;
    }
	thisone = gift_card_reader(input_fd);
	if (argv[1][0] == '1') print_gift_card_info(thisone);
    else if (argv[1][0] == '2') gift_card_json(thisone);

	return 0;
}