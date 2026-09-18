#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

#define TAM 50 

struct pessoa {
    char nome[TAM];
    int idade;
    float peso;
    float altura;
    char sexo;
};
typedef struct pessoa pessoa;
pessoa pes;

float Calcular_calorias(pessoa pes) {
    if (pes.sexo == 'M' || pes.sexo == 'm') {
        float calorias_m = (10 * pes.peso) + (6.25f * (pes.altura * 100)) - (5 * pes.idade) + 5;
        return calorias_m;
    }
    
    else {
        float calorias_f = (10 * pes.peso) + (6.25f * (pes.altura * 100)) - (5 * pes.idade) - 161;
        return calorias_f;
    }
}

int main() {

    printf("Qual seu nome? ");
    scanf("%s", pes.nome);
    printf("Qual sua idade? ");
    scanf("%d", &pes.idade);
    printf("Qual seu peso? ");
    scanf("%f", &pes.peso);
    printf("Qual sua altura? ");
    scanf("%f", &pes.altura);
    while (getchar() != '\n');
    printf("Qual seu sexo digitando M ou F? ");
    scanf("%c", &pes.sexo);

    printf("Suas calorias são: %.2f", Calcular_calorias(pes));

    return 0;
}