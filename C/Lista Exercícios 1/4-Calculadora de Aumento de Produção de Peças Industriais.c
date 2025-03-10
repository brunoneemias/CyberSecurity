#include <stdio.h>
#include <locale.h>

#define AUMENTO1 0.17
#define AUMENTO2 0.26
int main() {
    setlocale(LC_ALL, "pt_BR.UTF-8");

    float quantidade1, quantidade2, nova_quantidade1, nova_quantidade2;

    printf("Digite a quantidade atual da primeira peça: ");
    scanf("%f", &quantidade1);
    printf("Digite a quantidade atual da segunda peça: ");
    scanf("%f", &quantidade2);

    nova_quantidade1 = quantidade1 + (quantidade1 * aumento1);
    nova_quantidade2 = quantidade2 + (quantidade2 * aumento2);

    printf("A nova quantidade produzida da primeira peça é: %.2f\n", nova_quantidade1);
    printf("A nova quantidade produzida da segunda peça é: %.2f\n", nova_quantidade2);

    return 0;
}
