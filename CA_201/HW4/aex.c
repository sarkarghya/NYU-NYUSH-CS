#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct cell {
    char* key;
    struct cell *next;
};

/* Exercise 1.2 */
void print_list(struct cell *list){
    while (list != NULL){
        printf("%s\n", list->key);  // print the key
        // prints the elements of a list, one per line.
        list = list -> next;    // move to the next cell
    }
    return;
}

/* Exercise 1.3 */
int list_length(struct cell *list){
    int ln = 0;
    struct cell *tmplist = list;  
    while (tmplist != NULL){
        ln++;
        tmplist = tmplist->next;
    }
    return ln;
}

/* Exercise 1.1 */
struct cell *cons(char *string, struct cell *list){ 
    struct cell *newlist;  
    newlist = malloc(sizeof(struct cell));
    char* c = strdup(string);
    newlist -> key = c;  
    newlist -> next = list;  
return newlist;
}

/* Exercise 2.2 */
int *free_list(struct cell *list){ 
    struct cell *tmplist; 
    while (list != NULL){
        tmplist = list;
        list = list->next;
        free(tmplist);
    }
return 0;
}

/* Exercise 3.1 */
int list_member(char *string, struct cell *list){
    struct cell *tmplist = list;  
    while (tmplist != NULL){
        if (strcasecmp(tmplist->key, string) == 0){
            return 1;
        }
        tmplist = tmplist->next;
    }
    return 0;
}

int main(){
    /* Exercise 2.1 */
    struct cell *lisa = NULL;        //  empty list []
    lisa = cons("Today", lisa);
    lisa = cons("Weather", lisa);     
    lisa = cons("Beautiful", lisa);
    print_list(lisa);
    printf("Length of list: %d\n", list_length(lisa));

    /* Exercise 3.2 */
    if (list_member("Weather",lisa)){printf("Present\n");} else{printf("Absent\n");}
    if (list_member("Cloudy",lisa)){printf("Present\n");} else{printf("Absent\n");}

    /* Exercise 2.3 */
    free_list(lisa);
    //
    return 0;
}