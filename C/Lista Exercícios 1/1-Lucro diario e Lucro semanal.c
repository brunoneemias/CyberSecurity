#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese"); // Configura a localidade para exibir caracteres especiais corretamente

    float ganho_diario, gasto_diario, lucro_diario, lucro_total;
    int dias_semana = 5;

    // Solicita os valores de ganho e gasto diários
    printf("Digite o ganho diário: ");
    scanf("%f", &ganho_diario);
    printf("Digite o gasto diário: ");
    scanf("%f", &gasto_diario);

    // Calcula o lucro diário
    lucro_diario = ganho_diario - gasto_diario;

    // Calcula o lucro total da semana
    lucro_total = lucro_diario * dias_semana;

    // Exibe o lucro total da semana
    printf("O lucro total da semana é: %.2f\n", lucro_total);

    return 0;
}
