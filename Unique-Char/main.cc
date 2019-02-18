#include <stdio.h>
/* #include <stdlib.h> */

int main(){
    FILE *in;
    FILE *out;

    in = fopen("in.txt", "r");
    out = fopen("out.txt", "w");

    if (!out || !in) {
        fprintf(stderr, "\nError opening file\n");
        exit(1);
    }

    while(fscanf(&in, size)) {
        fprintf(out, &in);
        /* fprintf("Done!"); */
        /* fscanddf("This is life"); */
    }
    
    fclose(in);
    fclose(out);
}

