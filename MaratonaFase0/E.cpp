#include <iostream>
#include <numeric> // std::gcd

int main() {
    long long y, k;
    std::cin >> y >> k;

    long long x = 1;

    // Simula até atingir ponto onde X % Y == 0
    // (ou até que K acabe antes disso)
    while (k > 0) {
        long long g = std::gcd(x, y);
        x += g;
        k--;

        if (x % y == 0) {
            // Agora todo gcd(x, y) == y, então podemos pular direto
            x += k * y;
            break;
        }
    }

    std::cout << x << '\n';
    return 0;
}
