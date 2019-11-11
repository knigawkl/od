#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void readuser(void)
{
	/* czy należy przyznać dostęp */
	int ok;

	/* nikt przy zdrowych zmysłach nie będzie miał */
	/* nazwy użytkownika dłuższej niż 60 znaków */
	char user[60];

	ok = 0;

	puts("Podaj nazwę użytkownika:");
	gets(user);
	puts(user);

	if (strcmp(user, "root") == 0) {
		ok = 1;
	}

	if (strcmp(user, "r00t") == 0) {
		ok = 1;
	}

	if (ok) {
		puts("Dostęp przyznany.");
	} else {
		puts("Dostęp NIE przyznany.");
	}
}

int main(void)
{
	readuser();
	puts("Koniec.");
	return 0;
}
