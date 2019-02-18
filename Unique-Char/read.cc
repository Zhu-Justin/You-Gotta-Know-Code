#include <stdio.h>
int main() {
    FILE *read;
    FILE *write;
    const char* filename = "in.txt";
    read = fopen(filename, "r");
    if (!read) {
        write = fopen(filename, "w");
        fprintf(write, "%s", "hello");
        fclose(write);
    } else {
        char somedata[20];
        fscanf(read, "%s", somedata);
        printf("%s", somedata);
        fclose(read);
    }
    return 0;
}
