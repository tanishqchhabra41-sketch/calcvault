#include <stdio.h>
#include <string.h>

int main() {

    char input[100];

    scanf("%s", input);

    // SECRET CODE
    if(strcmp(input, "4582") == 0) {
        printf("VAULT");
        return 0;
    }

    int a, b;
    char op;

    sscanf(input, "%d%c%d", &a, &op, &b);

    switch(op) {

        case '+':
            printf("%d", a + b);
            break;

        case '-':
            printf("%d", a - b);
            break;

        case '*':
            printf("%d", a * b);
            break;

        case '/':
            if(b != 0)
                printf("%d", a / b);
            else
                printf("Error");
            break;

        default:
            printf("Error");
    }

    return 0;
}
