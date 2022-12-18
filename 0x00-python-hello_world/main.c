#include <stdio.h>
#include <stdlib.h>
#include "main.h"

int main(int argc, char **argv, char **env)
{
    (void) argc;
    (void) argv;
    (void) env;

    printf("%d) Hello World\n", argc);
    return (EXIT_SUCCESS);
}