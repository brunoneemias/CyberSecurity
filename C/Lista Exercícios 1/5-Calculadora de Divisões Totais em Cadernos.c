#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "pt_BR.UTF-8"); // Configura a localidade para Português do Brasil

    int num_cadernos, divisoes_por_caderno, total_divisoes;

    printf("Digite o número de cadernos: ");
    scanf("%d", &num_cadernos);
    printf("Digite o número de divisões por caderno: ");
    scanf("%d", &divisoes_por_caderno);

    total_divisoes = num_cadernos * divisoes_por_caderno;

    printf("O número total de divisões é: %d\n", total_divisoes);

    return 0;
}

