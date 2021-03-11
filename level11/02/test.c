#include <stdio.h>
#include <string.h>

int main() {
    char password[8];
    char solution[40] = "Recklt";
    strcat(password, "Rec");
    strcat(password, "klt");
    strcat(password, "");
    puts(password);
    const int equal = strcmp(password, solution);
    if (equal == 0) {
        puts("equal");
    } else {
        puts("not equal");
    }
}