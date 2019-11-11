#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* przykladowe zabezpieczenie przed buffer overflow */

int main(int argc, char *argv[]) {
    char zalogowany;
    char haslo[8];
    zalogowany = 'n';
    strncpy(haslo, argv[1], 8);
    if( strcmp( haslo, "tajne" ) == 0 ){
        zalogowany = 't';
    }
    if( zalogowany == 't' ){
        printf("Poprawne haslo, witamy :)\n");
	return 0;
    } else {
        printf("Bledne haslo, uciekaj :(\n");
	return 1;
    }
}
