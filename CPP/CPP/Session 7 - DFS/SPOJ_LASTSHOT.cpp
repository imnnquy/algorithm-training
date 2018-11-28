//  Problem from SPOJ
//  https://www.spoj.com/problems/LASTSHOT/

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int findMaximum(int N, vector<vector<int>> graph) {
    int maxImpact = 0;

    for(int i = 1; i <= N; i++) {
        vector<bool> visited;
        for(int x = 0; x <= N; x++) {
            visited.push_back(false);
        }
        int currentImpact = 1;
        stack<int> s;
        s.push(i);
        visited[i] = true;
        while(s.size() > 0) {
            int u = s.top();
            s.pop();
            for(int j = 0; j < graph[u].size(); j++) {
                int v = graph[u][j];
                if(!visited[v]) {
                    s.push(v);
                    visited[v] = true;
                    currentImpact++;
                }
            }
        }
        if(currentImpact > maxImpact){
            maxImpact = currentImpact;
        }

    }
    return maxImpact;
}

int main() {
    int N, M;
    vector<vector<int>> graph;
    cin >> N >> M;
    for(int i = 0; i < N+1; i++) {
        graph.push_back(vector<int>());
    }

    for(int i = 0; i < M; i++) {
        int A, B;
        cin >> A >> B;
        graph[A].push_back(B);
    }
    cout << findMaximum(N, graph);

    return 0;
}
