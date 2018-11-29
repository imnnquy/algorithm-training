// Problem from URI
// https://www.urionlinejudge.com.br/judge/en/problems/view/1610


#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

string sim_nao(int N, vector<vector<int>> &graph) {
    vector<bool> global_visited;
    for(int i = 0; i <= N; i++) {
        global_visited.push_back(false);
    }

    for (int i = 1; i <= N; i++) {
        if(!global_visited[i]){
            vector<bool> visited;
            for (int j = 0; j <= N; j++) {
                visited.push_back(false);
            }
            stack<int> s;
            s.push(i);
            global_visited[i] = true;
            visited[i] = true;
            vector<int> path;
            for (int p = 0; p <= N; p++) {
                path.push_back(-1);
            }
            while (s.size() > 0) {
                int u = s.top();
                s.pop();
                for(int k = 0; k < graph[u].size(); k++) {
                    int v = graph[u][k];
                    if (!visited[v]) {
                        s.push(v);
                        visited[v] = true;
                        global_visited[u] = true;
                        path[v] = u;
                    } else {
                        int f = u;
                        while (true) {
                            f = path[f];
                            if (f == -1) {
                                break;
                            }
                            if(f == v) {
                                return "SIM";
                            }
                        }
                    }
                }
            }

        }
    }
    return "NAO";
}

int main() {
    vector<string> results;
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {

        int N, M;
        cin >> N >> M;

        vector<vector<int>> graph;
        for(int i = 0; i <= N; i++) {
            graph.push_back(vector<int>());
        }
        
        for(int j = 0; j < M; j++) {
            int A, B;
            cin >> A >> B;
            
            vector<int>::iterator it = find (graph[A].begin(), graph[A].end(), B);
            if(it == graph[A].end()) {
                graph[A].push_back(B);
            }
            
        }
        results.push_back(sim_nao(N, graph));

    }
    for(int i = 0; i < results.size() - 1; i++) {
        std::cout << results[i] << std::endl;
    }
    if (results.size() > 0) {
        cout << results[results.size() - 1] << endl;
    }
}