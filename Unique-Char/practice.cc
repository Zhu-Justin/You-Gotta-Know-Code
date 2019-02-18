#include <stdio.h>
#include <stdlib.h>

int main() {
    char str1[10], str2[10], str3[10];
    int year;
    FILE * fp;
    fp = fopen ("in.txt", "w+");
    fputs("We are in 2012", fp);

    rewind(fp);
    fscanf(fp, "%s %s %s %d", str1, str2, str3, &year);

    printf("%s\n", str1);
    printf("%s\n", str2);
    printf("%s\n", str3);
    printf("%d\n", year);

}

