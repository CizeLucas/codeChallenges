#include <iostream>
#include <vector>

int main() {
    int N, K;
    std::cin >> N >> K;

    std::vector<int> A(N);
    for (int i = 0; i < N; i++) {
        std::cin >> A[i];
    }

    std::vector<int> B;

    for (int i = 0; i < N; i++) {
        int fase = A[i];
        int filtro = A[i];
        int filterIndex = i;

        while (true) {
            if (fase > filtro) {
                B.push_back(filterIndex + 1); // +1 para manter índice 1-based
                break;
            } else {
                fase += K;
                filterIndex++;
                if (filterIndex >= N)
                    filterIndex = 0;
                filtro = A[filterIndex];
            }
        }
    }

    // Impressão sem colchetes nem vírgulas
    for (int i = 0; i < B.size(); i++) {
        std::cout << B[i];
        if (i != B.size() - 1)
            std::cout << " ";
    }


    return 0;
}
