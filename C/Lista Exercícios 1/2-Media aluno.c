#include <stdio.h>
#include <locale.h>

#define PESO1 0.4
#define PESO2 0.6

int main() {
    setlocale(LC_ALL, ""); // Configura a localidade para exibir caracteres especiais corretamente

    float nota1, nota2, media_final;

    // Solicita as notas do aluno
    printf("Digite a primeira nota: ");
    scanf("%f", &nota1);
    printf("Digite a segunda nota: ");
    scanf("%f", &nota2);

    // Calcula a média final
    media_final = (nota1 * PESO1) + (nota2 * PESO2);

    // Exibe a média final
    printf("A média final é: %.2f\n", media_final);

    return 0;
}
