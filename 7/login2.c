#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char zalogowany;	
    char haslo[8];
    zalogowany = 'n';
    strcpy( haslo, argv[1] );
    if(strcmp(haslo, "tajne") == 0){
        printf("Poprawne haslo, witamy :)\n");
    } else {
        printf("Bledne haslo, uciekaj :(\n");
    }
    return 0;
}
