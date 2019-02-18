#include <stdio.h>

int main() {
    FILE * fp;
    int i, n;
    char str[100];
    char fname[20]="in.txt";
    char * fout = "out.txt";
    char str1;
    scanf("%d", &n);
    printf("\n :: Lines are :: \n");
    fp = fopen(fname, "w");
    int c = fgets(str, sizeof(str), stdin);
    while (i != 
    for (i) {
        fgets(str, sizeof(str), stdin);
        fputs(str, fp);
    }
    fclose(fp);
    fp = fopen(fname, "r");
    printf("The content of the file is %s", fname);
    str1 = fgetc(fp);
    while (str1 != EOF) {
        printf("%c", str1);
        str1 = fgetc(fp);
    }
    printf("\n\n");
    fclose(fp);
    return 0;
}
