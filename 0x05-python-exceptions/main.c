#include <stdio.h>
#include <stdlib.h>

int main() {
    double f = 19492307816406286;// very small value
    double factor = 1e-300; // factor to shift decimal point
    double g = f * factor; // shift decimal point
    int i = (int)g; // convert double to int
    double h = (double)i / factor; // convert int back to double and shift decimal point back
    if (f == h) {
        printf("%.10e is a whole number\n", f);
    } else {
        printf("%.10e is not a whole number\n", f);
    }
    return 0;
}
