//  Problem from SPOJ
//  https://www.spoj.com/problems/CAM5/

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int calc_disjoint_sets(int Ni, vector<vector<int>> graph) {
    int result = 0;
    vector<bool> visited;
    for(int i = 0; i < Ni; i++) {
        visited.push_back(false);
    }
    for (int i = 0; i < Ni; i++) {
        if(visited[i]){
            continue;
        } else {
            stack<int> s;
            s.push(i);
            visited[i] = true;
            while (!s.empty()){
                int u = s.top();
                s.pop();
                for (int j = 0; j < graph[u].size(); j++) {
                    int v = graph[u][j];
                    if (!visited[v]) {
                        visited[v] = true;
                        s.push(v);
                    }
                }
            }
            result++;
        }
    }

    return result;
}

int main()
{
    int t;
    vector<int> results = vector<int>();
    cin >> t;
    for(int i = 0; i < t; i++) {
        int Ni, ei;
        cin >> Ni;
        cin >> ei;
        vector<vector<int>> graph;
        for(int j = 0; j < Ni; j++) {
            graph.push_back(vector<int>());
        }
        for(int j = 0; j < ei; j++) {
            int start, end;
            cin >> start >> end;
            graph[start].push_back(end);
            graph[end].push_back(start);
        }
        results.push_back(calc_disjoint_sets(Ni, graph));
    }
    for(int i = 0; i < results.size() - 1; i++) {
        std::cout << results[i] << std::endl;
    }
    if (results.size() > 0) {
        cout << results[results.size() - 1];
    }
    return 0;
}

