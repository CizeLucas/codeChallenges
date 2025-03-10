/*
Leia 4 valores inteiros A, B, C e D.
A seguir, se B for maior do que C 
e se D for maior do que A, 
e a soma de C com D for maior que a soma de A e B 
e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores:

Exemplo de Entrada  |   Exemplo de Saída
5 6 7 8             |   Valores nao aceitos
2 3 2 6             |   Valores aceitos
*/
#include <stdio.h>
int main() {

int A = 0;
int B = 0;
int C = 0;
int D = 0;

scanf("%d", &A);
scanf("%d", &B);
scanf("%d", &C);
scanf("%d", &D);


if(B > C && D > A && (C+D) > (A+B) && C > 0 && D > 0 && A%2==0)
    printf("Valores aceitos\n");
else
    printf("Valores nao aceitos\n");
}

//Printar os 6 números impares apartir de um número de entrada (incluso ele mesmo)
#include <stdio.h>
 
int main() {
 
    int startNumber = 0;
    scanf("%d", &startNumber);
    
    for(int i = startNumber; i<=startNumber+11; i++) {
        if(i%2 != 0)
            printf("%d\n", i);
    }
    return 0;
    
    // 2 3 X 5 X 7 X 9 X 11 X 13
    // 8 9 X 11 X 13 X 15 X 17 X 19
}
