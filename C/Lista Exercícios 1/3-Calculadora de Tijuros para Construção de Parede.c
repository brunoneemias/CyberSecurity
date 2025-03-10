#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "pt_BR.UTF-8");

    float altura_parede, largura_parede, comprimento_tijolo, largura_tijolo, area_parede, area_tijolo;
    int quantidade_tijolos;


    printf("Digite a altura da parede (em metros): ");
    scanf("%f", &altura_parede);
    printf("Digite a largura da parede (em metros): ");
    scanf("%f", &largura_parede);
    printf("Digite o comprimento do tijolo (em metros): ");
    scanf("%f", &comprimento_tijolo);
    printf("Digite a largura do tijolo (em metros): ");
    scanf("%f", &largura_tijolo);

    area_parede = altura_parede * largura_parede;
    area_tijolo = comprimento_tijolo * largura_tijolo;

    quantidade_tijolos = (int)(area_parede / area_tijolo);

    printf("A quantidade de tijolos necessária é: %d\n", quantidade_tijolos);

    return 0;
}
