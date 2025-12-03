#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <tuple>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);

    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int Q;
    cin >> Q;
    vector<int> queries(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> queries[i];
    }

    // Mapeia soma de pares para todos os pares possíveis
    unordered_map<int, vector<pair<int, int>>> pair_sums;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            int sum = A[i] + A[j];
            pair_sums[sum].emplace_back(i, j);
        }
    }

    for (int q = 0; q < Q; ++q) {
        int target = queries[q];
        set<tuple<int, int, int, int>> unique_quads;
        int count = 0;

        for (const auto& [s1, pairs1] : pair_sums) {
            int s2 = target - s1;
            if (!pair_sums.count(s2)) continue;

            const auto& pairs2 = pair_sums[s2];

            for (const auto& [i1, j1] : pairs1) {
                for (const auto& [i2, j2] : pairs2) {
                    set<int> indices = {i1, j1, i2, j2};
                    if (indices.size() == 4) {
                        vector<int> sorted_idx(indices.begin(), indices.end());
                        unique_quads.emplace(sorted_idx[0], sorted_idx[1], sorted_idx[2], sorted_idx[3]);
                    }
                }
            }
        }

        cout << unique_quads.size() << endl;
    }

    return 0;
}
