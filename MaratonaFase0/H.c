#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Converte um número inteiro para binário como string
void to_binary(int num, char *bin_str) {
    int idx = 0;
    while (num > 0) {
        bin_str[idx++] = (num % 2) + '0';
        num /= 2;
    }
    bin_str[idx] = '\0';

    // Inverter a string binária para que fique na ordem correta
    for (int i = 0; i < idx / 2; i++) {
        char tmp = bin_str[i];
        bin_str[i] = bin_str[idx - i - 1];
        bin_str[idx - i - 1] = tmp;
    }
}

// Verifica se a string binária é palíndroma
bool is_palindrome(const char *s) {
    int len = strlen(s);
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int X;
    scanf("%d", &X);

    int Y = (X % 2 == 0) ? X - 1 : X;

    char bin[64];

    while (Y >= 1) {
        to_binary(Y, bin);
        if (is_palindrome(bin)) {
            break;
        }
        Y -= 2;
    }

    printf("%d\n", Y);

    return 0;
}
